import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# 1. Setup the credentials
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def list_supported_models():
    print("--- AVAILABLE GOOGLE MODELS ---")
    # 2. Call the list_models function
    # We filter for 'generateContent' to find models that work with your summary script
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"ID: {model.name} | Display Name: {model.display_name}")

if __name__ == "__main__":
    list_supported_models()