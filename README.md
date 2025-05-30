# Gemini LangGraph Chat App

This project demonstrates a simple interactive chat application using Google's Gemini model and LangGraph. It fetches Gemini account details and allows users to chat with the AI in a conversational loop.

## Features
- Fetches and displays Gemini account information (available models, current model details).
- Interactive chat interface where users can send messages and receive responses from Gemini.
- Built using LangGraph for workflow management.

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
4. Run the chat app:
   ```
   python3 chat_app.py
   ```

## Usage
- Start the app and follow the prompts to chat with Gemini.
- Type `exit` or `quit` to end the chat session.

## Dependencies
- langgraph
- langchain
- langchain-google-genai
- python-dotenv
- google-generativeai 