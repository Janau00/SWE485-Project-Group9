#Imports & Client Setup
import os
from google import genai
from dotenv import load_dotenv, find_dotenv

load_dotenv(override=True)  
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
MODEL = "gemini-2.5-flash"

#Shared Method
def call_gemini(system_prompt, user_prompt):
    response = client.models.generate_content(
        model=MODEL,
        contents=user_prompt,
        config={"system_instruction": system_prompt}
    )
    return response.text
