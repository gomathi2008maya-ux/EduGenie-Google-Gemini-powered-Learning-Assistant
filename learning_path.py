import os
from google import genai

def get_learning_recommendations(topic: str, level: str = "beginner", hours_per_week: float = 5.0):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "GEMINI_API_KEY is missing. Please check your .env file."

    client = genai.Client(api_key=api_key)

    prompt = f"""
    Create a learning plan for the topic: {topic}
    Student level: {level}
    Study time per week: {hours_per_week} hours.

    Give a step-by-step learning roadmap with topics, activities,
    and suggested weekly schedule.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text