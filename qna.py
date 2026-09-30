import os
from google import genai

def answer_question(question: str):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "GEMINI_API_KEY is missing. Please check your .env file."

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=question
    )

    return response.text