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

# Example product details with Amazon pricing and inventory
shoe_details = {
    "Nike Air Max": {
        "description": "The Nike Air Max is a classic sneaker known for its comfort and style. It features a cushioned sole and is available in various colors.",
        "price": "$120",
        "inventory": "In Stock"
    },
    "Adidas Ultraboost": {
        "description": "The Adidas Ultraboost is a high-performance running shoe with responsive cushioning and a sleek design.",
        "price": "$180",
        "inventory": "In Stock"
    },
    "Puma RS-X": {
        "description": "The Puma RS-X is a retro-inspired sneaker with a bold design and comfortable fit.",
        "price": "$100",
        "inventory": "Low Stock"
    }
}

# Function to place an order
def place_order(shoe_name):
    if shoe_name in shoe_details:
        if shoe_details[shoe_name]["inventory"] == "In Stock":
            print(f"Order placed for {shoe_name} at {shoe_details[shoe_name]['price']}.")
            return True
        else:
            print(f"Sorry, {shoe_name} is currently out of stock.")
            return False
    else:
        print(f"Sorry, {shoe_name} is not available.")
        return False

# Run the graph
if __name__ == "__main__":
    # Get account information
    account_info = get_account_info()
    print("\nGemini Account Information:")
    print("------------------------")
    for key, value in account_info.items():
        print(f"{key}: {value}")
    print("------------------------\n")

    print("Welcome to the E-commerce Chatbot!")
    print("Type your message and press Enter to chat with the bot.")
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
            print(f"Bot: {ai_message.content}\n")
            # Check if the user is asking about shoes
            if "shoe" in user_input.lower() or "shoes" in user_input.lower():
                print("Here are some details about our shoes:")
                for shoe, details in shoe_details.items():
                    print(f"{shoe}: {details['description']}")
                    print(f"Price: {details['price']}, Inventory: {details['inventory']}\n")
            # Check if the user wants to place an order
            elif "order" in user_input.lower():
                for shoe in shoe_details:
                    if shoe.lower() in user_input.lower():
                        place_order(shoe)
                        break
        else:
            print("Bot: (No response)\n") 