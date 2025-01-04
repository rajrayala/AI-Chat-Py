import os
from dotenv import load_dotenv
from ollama import chat
from ollama import ChatResponse, Options

load_dotenv()

class OllamaModel:
    def __init__(self):
        self.model_name = os.getenv("OLLAMA_MODEL_NAME")

    def chat(self, config):
        options = Options(temperature=config.temperature)
        response: ChatResponse = chat(
            model=self.model_name,
            stream=config.stream,
            options=options,
            messages=[{'role': 'user', 'content': config.user_input}],
        )
        if config.stream:
            for part in response:
                yield part.message.content  # Yield each part of the response
        else:
            return response.message.content if response else "No response from model."