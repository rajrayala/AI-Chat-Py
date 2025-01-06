import os
from dotenv import load_dotenv
from ollama import chat
from ollama import Options

load_dotenv()

class OllamaModel:
    def __init__(self):
        self.model_name = os.getenv("OLLAMA_MODEL_NAME")

    def chat(self, config):
        options = Options(temperature=config.temperature)
        response = chat(
            model=self.model_name,
            stream=config.stream,
            options=options,
            messages=[{'role': 'user', 'content': config.user_input}],
        )
        
        # Streaming logic
        if config.stream:
            return (part.message.content for part in response if part.message.content)
        
        # Non-streaming logic
        return response.message.content if response and response.message.content else "No response from model."