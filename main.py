import os
from models.ollama_model import OllamaModel
from models.mistral_model import MistralModel
from models.gemini_model import GeminiModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    def __init__(self, user_input, temperature, stream=False):
        self.user_input = user_input
        self.temperature = temperature
        self.stream = stream

def main():
    # Initialize models
    models = {
        "Ollama": OllamaModel(),
        "Mistral": MistralModel(),
        "Gemini": GeminiModel(),
    }

    print("Welcome to the Chatbot!")
    print("Select a model to chat with:")
    for i, model_name in enumerate(models.keys(), start=1):
        print("{}. {}".format(i, model_name))

    # Model selection
    model_choice = int(input("Enter the number of the model you want to use: ")) - 1
    selected_model = list(models.values())[model_choice]

    print("You selected: {}".format(list(models.keys())[model_choice]))

    # Initialize context
    context = []
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat. Goodbye!")
            break
        if user_input.lower() in ["new", "new chat", "clear"]:
            context = []
            print("Cleared the chat history.")
            continue
        
        # Append user input to context
        context.append({"role": "user", "content": user_input})

        # Limit context to the last few exchanges
        if len(context) > 6:
            context = context[-6:]

        # Create a context-aware input for the model
        context_input = "\n".join([f"{msg['role']}: {msg['content']}" for msg in context]) + "\nAssistant:"

        config = Config(context_input, 0.7, True)
        response = selected_model.chat(config)
        full_response = ""
        if config.stream:
            print("{}: ".format(list(models.keys())[model_choice], end='', flush=True))
            for part in response:
                full_response += part  # Accumulate the response
                print(part, end='', flush=True)
            print()
        else:
            full_response = response
            print("{}: {}".format(list(models.keys())[model_choice], response))
        
        # Append AI response to context
        context.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()