import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()

class MistralModel:
    def __init__(self):
        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.model_name = os.getenv("MISTRAL_MODEL_NAME")
        self.client = Mistral(api_key=self.api_key)

    def chat(self, config):
        if config.stream:
            chat_response = self.client.chat.stream(
                model=self.model_name,
                temperature=config.temperature,
                messages=[{"role": "user", "content": config.user_input}]
            )
            for chunk in chat_response:
                yield chunk.data.choices[0].delta.content # Yield each part of the response
        else:
            chat_response = self.client.chat.complete(
                model=self.model_name,
                temperature=config.temperature,
                messages=[{"role": "user", "content": config.user_input}]
            )
            return chat_response.choices[0].message.content if chat_response.choices else "No response from model."
