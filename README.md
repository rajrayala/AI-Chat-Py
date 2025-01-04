# Chat with Multiple AI Models

This project is a command-line chat that allows users to interact with different AI models, including Ollama, Mistral, and Gemini. The chat maintains context across conversations, providing a more coherent and engaging user experience.

## Features

- **Model Selection**: Choose between Ollama, Mistral, and Gemini models.
- **Context Management**: Maintains a history of user inputs and AI responses for context-aware conversations.
- **Streaming Responses**: Supports both streaming and non-streaming responses from the models.
- **Clear Chat History**: Users can clear the chat history at any time.

## Requirements

- Python 3.7 or higher
- Required libraries:
  - `dotenv`
  - `ollama` (for Ollama model)
  - `mistralai` (for Mistral model)
  - `google.generativeai` (for Gemini model)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rajrayala/ai-chat-py.git
2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
3. Create a .env file in the root directory of the project and add your API keys and model names:
    ```text
    OLLAMA_MODEL_NAME=your_ollama_model_name
    MISTRAL_API_KEY=your_mistral_api_key
    MISTRAL_MODEL_NAME=your_mistral_model_name
    GEMINI_API_KEY=your_gemini_api_key
    GEMINI_MODEL_NAME=your_gemini_model_name
    ```

## Usage
1. Run the chat app:
    ```bash
    python main.py
2. Follow the prompts to select a model and start chatting. You can type your messages and receive responses from the selected AI model.
3. Use the following commands during the chat:
    Type exit or quit to end the conversation.
    Type new, new chat, or clear to clear the chat history.

## Example Interaction
```text
    Welcome to the Chatbot!
    Select a model to chat with:
    1. Ollama
    2. Mistral
    3. Gemini
    Enter the number of the model you want to use: 1
    You selected: Ollama
    You: Hello
    Ollama: Hi there! How can I assist you today?
```

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.