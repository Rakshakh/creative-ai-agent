import openai
import os
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_response(prompt, model="gpt-4o", temperature=0.7):
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error] {str(e)}"
