# E-commerce Chatbot

This chatbot helps users browse products and place orders for shoes. It uses Google's Gemini model to generate responses and provides details about available shoes, including pricing and inventory status.

## Features
- Interactive chat interface for browsing shoes.
- Provides detailed information about shoes, including descriptions, prices, and inventory status.
- Simulates order placement for available shoes.

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
1. **Start the E-commerce Chatbot:**
   - Run the chatbot using the command:
     ```
     python3 ecommerce_chatbot.py
     ```

2. **Interact with the Bot:**
   - Ask about shoes to get details, pricing, and inventory information.
   - Place an order by mentioning the shoe name and the word "order."

3. **End the Chat:**
   - Type `exit` or `quit` to end the chat session.

## Example Interaction
```
You: Tell me about Nike Air Max
Bot: Nike Air Max: The Nike Air Max is a classic sneaker known for its comfort and style. It features a cushioned sole and is available in various colors.
Price: $120, Inventory: In Stock

You: I want to order Nike Air Max
Bot: Order placed for Nike Air Max at $120.
``` 