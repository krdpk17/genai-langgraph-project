# LangGraph Hello World

This is a simple example project demonstrating the basic usage of LangGraph, a framework for building stateful, multi-actor applications with LLMs.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Example

Run the example with:
```bash
python hello_world.py
```

## How it Works

This example demonstrates a simple LangGraph workflow that:
1. Takes an input message
2. Processes it through multiple steps
3. Generates a response using an LLM
4. Returns the final result

The graph consists of two main nodes:
- `process_input`: Handles the initial message processing
- `generate_response`: Uses the LLM to generate a response

The workflow demonstrates basic LangGraph concepts like:
- State management
- Node definition
- Edge creation
- Conditional routing
- Graph compilation and execution 