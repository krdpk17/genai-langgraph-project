# Simple Chat App

This is a simple interactive chat application using Google's Gemini model and LangGraph. It fetches Gemini account details and allows users to chat with the AI in a conversational loop.

## Features
- Fetches and displays Gemini account information (available models, current model details).
- Interactive chat interface where users can send messages and receive responses from Gemini.
- Simple command-line UI for user interaction.
- Built using LangGraph for workflow management.

## Setup
1. Ensure you have the required dependencies installed:
   ```
   pip install -r requirements.txt
   ```
2. Set your Google API key in a `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage Guide
1. **Start the Chat App:**
   - Run the app using the command:
     ```
     python3 chat_app.py
     ```

2. **Interact with Gemini:**
   - Type your message and press Enter to send it to Gemini.
   - Gemini will respond to your message in the chat.

3. **End the Chat:**
   - Type `exit` or `quit` to end the chat session.

## Example Interaction
```
You: hi
Gemini: Hi there! How can I help you today?

You: 2+3 equals
Gemini: 2 + 3 = 5

You: i need first 5 numbers in fibonacci series
Gemini: The first 5 numbers in the Fibonacci sequence are: 1, 1, 2, 3, 5

You: please give sum of them
Gemini: The sum of the first 5 Fibonacci numbers is: 1 + 1 + 2 + 3 + 5 = 12

You: bye
Gemini: Goodbye!
``` 