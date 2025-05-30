from typing import Annotated, TypedDict
from langgraph.graph import Graph, StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the state
class State(TypedDict):
    messages: list[HumanMessage]
    current_step: str
    account_info: dict

def get_account_info() -> dict:
    """Fetch Gemini account information."""
    try:
        # Get model information
        models = genai.list_models()
        available_models = [model.name for model in models]
        
        # Get current model details
        current_model = genai.get_model("gemini-2.0-flash")
        
        return {
            "available_models": available_models,
            "current_model": current_model.name,
            "model_description": current_model.description,
            "model_generation_config": current_model.supported_generation_methods
        }
    except Exception as e:
        return {"error": str(e)}

# Define the nodes
def process_input(state: State) -> State:
    """Process the initial input."""
    print("Processing input...")
    return {
        "messages": state["messages"],
        "current_step": "processed",
        "account_info": state.get("account_info", {})
    }

def generate_response(state: State) -> State:
    """Generate a response using the LLM."""
    print("Generating response...")
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    response = llm.invoke(state["messages"])
    state["messages"].append(response)
    return {
        "messages": state["messages"],
        "current_step": "completed",
        "account_info": state.get("account_info", {})
    }

def should_end(state: State) -> str:
    """Determine if we should end the graph."""
    return "end" if state["current_step"] == "completed" else "continue"

# Create the graph
workflow = StateGraph(State)

# Add nodes
workflow.add_node("process", process_input)
workflow.add_node("generate", generate_response)
workflow.add_node("end", lambda state: state)

# Add edges
workflow.add_edge("process", "generate")
workflow.add_conditional_edges(
    "generate",
    should_end,
    {
        "continue": "process",
        "end": "end"
    }
)

# Set the entry point
workflow.set_entry_point("process")

# Compile the graph
app = workflow.compile()

# Run the graph
if __name__ == "__main__":
    # Get account information
    account_info = get_account_info()
    print("\nGemini Account Information:")
    print("------------------------")
    for key, value in account_info.items():
        print(f"{key}: {value}")
    print("------------------------\n")

    print("Welcome to the Gemini Chat App!")
    print("Type your message and press Enter to chat with Gemini.")
    print("Type 'exit' or 'quit' to end the chat.\n")
    messages = []
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        messages.append(HumanMessage(content=user_input))
        state = {
            "messages": messages.copy(),
            "current_step": "start",
            "account_info": account_info
        }
        result = app.invoke(state)
        # Find the latest AI message
        ai_message = next((m for m in result["messages"][::-1] if m.type == "ai"), None)
        if ai_message:
            print(f"Gemini: {ai_message.content}\n")
        else:
            print("Gemini: (No response)\n") 