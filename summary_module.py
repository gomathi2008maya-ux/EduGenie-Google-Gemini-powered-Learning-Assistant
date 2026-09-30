import os
from google import genai

def summarize_text(text: str):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "GEMINI_API_KEY is missing. Please check your .env file."

    client = genai.Client(api_key=api_key)

    prompt = f"Summarize the following text in simple language:\n\n{text}"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text