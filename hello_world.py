from typing import Annotated, TypedDict
from langgraph.graph import Graph, StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the state
class State(TypedDict):
    messages: list[HumanMessage]
    current_step: str

# Define the nodes
def process_input(state: State) -> State:
    """Process the initial input."""
    print("Processing input...")
    return {"messages": state["messages"], "current_step": "processed"}

def generate_response(state: State) -> State:
    """Generate a response using the LLM."""
    print("Generating response...")
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    response = llm.invoke(state["messages"])
    state["messages"].append(response)
    return {"messages": state["messages"], "current_step": "completed"}

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
    # Initialize the state
    initial_state = {
        "messages": [HumanMessage(content="Hello, World!")],
        "current_step": "start"
    }
    
    # Run the graph
    result = app.invoke(initial_state)
    
    # Print the final messages
    for message in result["messages"]:
        print(f"{message.type}: {message.content}") 