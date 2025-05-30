# Gemini LangGraph Project

This project contains two interactive chat applications built using Google's Gemini model and LangGraph:

1. **Simple Chat App:** A basic chat application that allows users to interact with the Gemini model.
2. **E-commerce Chatbot:** A chatbot that helps users browse shoes and place orders.

## Project Structure
- `simple_chat_bot/`: Contains the simple chat app and its documentation.
- `ecommerce_bot/`: Contains the e-commerce chatbot and its documentation.

## Setup
1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your Google API key in a `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage
- For the Simple Chat App, navigate to the `simple_chat_bot` directory and follow the instructions in its README.
- For the E-commerce Chatbot, navigate to the `ecommerce_bot` directory and follow the instructions in its README.

## Dependencies
- langgraph
- langchain
- langchain-google-genai
- python-dotenv
- google-generativeai 