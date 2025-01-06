import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class GeminiModel:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model_name = os.getenv("GEMINI_MODEL_NAME")
        genai.configure(api_key=self.api_key)

    def chat(self, config):
        model = genai.GenerativeModel(self.model_name)
        generation_config = genai.GenerationConfig(temperature=config.temperature)

        response = model.generate_content(
            contents=config.user_input, 
            stream=config.stream, 
            generation_config=generation_config
        )

        # Streaming logic
        if config.stream:
            return (chunk.text for chunk in response if chunk.text)
        
        # Non-streaming logic
        return response.text if response and response.text else "No response from Gemini model."