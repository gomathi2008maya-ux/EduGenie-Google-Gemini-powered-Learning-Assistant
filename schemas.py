from typing import Any
from pydantic import BaseModel

class QARequest(BaseModel):
    question: str

class QAResponse(BaseModel):
    answer: str

class ExplainRequest(BaseModel):
    topic: str
    level: str = "beginner"

class ExplainResponse(BaseModel):
    explanation: str

class QuizRequest(BaseModel):
    text: str
    topic: str = ""

class QuizResponse(BaseModel):
    quiz: Any

class SummaryRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str

class LearnRequest(BaseModel):
    topic: str
    level: str = "beginner"
    hours_per_week: float = 5.0

class LearnResponse(BaseModel):
    recommendations: Any