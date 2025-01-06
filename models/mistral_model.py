import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()

class MistralModel:
    def __init__(self):
        self.client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
        self.model_name = os.getenv("MISTRAL_MODEL_NAME")

    def chat(self, config):
        chat_method = self.client.chat.stream if config.stream else self.client.chat.complete
        
        chat_response = chat_method(
            model=self.model_name,
            temperature=config.temperature,
            messages=[{"role": "user", "content": config.user_input}]
        )
        
        # Streaming logic
        if config.stream:
            return (chunk.data.choices[0].delta.content for chunk in chat_response 
                    if chunk.data.choices[0].delta.content is not None)
        
        # Non-streaming logic
        return chat_response.choices[0].message.content if chat_response.choices else "No response from Mistral API."