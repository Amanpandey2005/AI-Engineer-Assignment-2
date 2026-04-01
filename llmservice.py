import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    def __init__(self):
        # Using Hugging Face Inference API 
        self.client = OpenAI(
            base_url="https://api-inference.huggingface.co/v1/",
            api_key=os.getenv("HF_TOKEN")
        )

    def analyze_sentiment(self, text):
        try:
            response = self.client.chat.completions.create(
                model="mistralai/Mistral-7B-Instruct-v0.2", 
                messages=[
                    {"role": "system", "content": "Provide a concise 1-sentence sentiment summary."},
                    {"role": "user", "content": text}
                ],
                max_tokens=100
            )
            return response.choices[0].message.content
        except Exception as e:
          return f"API Error: {str(e)}"