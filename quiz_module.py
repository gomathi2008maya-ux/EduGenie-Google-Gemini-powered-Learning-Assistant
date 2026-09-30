import os
from google import genai

def generate_quiz(text: str, topic: str = ""):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "GEMINI_API_KEY is missing. Please check your .env file."

    client = genai.Client(api_key=api_key)

    prompt = f"""
    Create 5 multiple-choice quiz questions based on this text.
    Topic: {topic}
    Text: {text}
    Include four options and the correct answer for each question.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text