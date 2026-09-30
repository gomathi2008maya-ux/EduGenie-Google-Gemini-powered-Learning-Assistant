import os
from google import genai

def explain_topic(topic: str, level: str = "beginner"):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "GEMINI_API_KEY is missing. Please check your .env file."

    client = genai.Client(api_key=api_key)

    prompt = f"""
    Explain the topic '{topic}' for a {level} level student.
    Use simple language and examples.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text