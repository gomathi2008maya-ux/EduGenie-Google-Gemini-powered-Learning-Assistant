from pathlib import Path

from fastapi import (
    FastAPI,
    HTTPException,
    Request,
)

from fastapi.responses import HTMLResponse

from fastapi.staticfiles import (
    StaticFiles,
)

from fastapi.templating import (
    Jinja2Templates,
)

from schemas import (
    ExplainRequest,
    LearnRequest,
    QARequest,
    QuizRequest,
    SummaryRequest,
    ExplainResponse,
    LearnResponse,
    QAResponse,
    QuizResponse,
    SummaryResponse,
)

from explanation_module import (
    explain_topic,
)

from qna import (
    answer_question,
)

from quiz_module import (
    generate_quiz,
)

from summary_module import (
    summarize_text,
)

from learning_path import (
    get_learning_recommendations,
)


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title=(
        "EduGenie - "
        "Google Gemini Powered "
        "Learning Assistant"
    ),
    version="1.0.0",
    description=(
        "A lightweight educational "
        "assistant for Q&A, explanations, "
        "quizzes, summaries, and learning paths."
    ),
)


app.mount(
    "/static",
    StaticFiles(
        directory=BASE_DIR / "static"
    ),
    name="static",
)


templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


@app.get(
    "/",
    response_class=HTMLResponse,
)
async def home(
    request: Request,
):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.get("/health")
async def health():

    return {
        "status": "ok",
        "service": "EduGenie",
    }


@app.post(
    "/qa",
    response_model=QAResponse,
)
async def qa(
    payload: QARequest,
):

    try:

        return QAResponse(
            answer=answer_question(
                payload.question
            )
        )

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc),
        ) from exc


@app.post(
    "/explain",
    response_model=ExplainResponse,
)
async def explain(
    payload: ExplainRequest,
):

    try:

        return ExplainResponse(
            explanation=explain_topic(
                payload.topic,
                payload.level,
            )
        )

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc),
        ) from exc


@app.post(
    "/quiz",
    response_model=QuizResponse,
)
async def quiz(
    payload: QuizRequest,
):

    try:

        return QuizResponse(
            quiz=generate_quiz(
                payload.text,
                payload.topic,
            )
        )

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc),
        ) from exc


@app.post(
    "/summarize",
    response_model=SummaryResponse,
)
async def summarize(
    payload: SummaryRequest,
):

    try:

        return SummaryResponse(
            summary=summarize_text(
                payload.text
            )
        )

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc),
        ) from exc


@app.post(
    "/learn/recommendations",
    response_model=LearnResponse,
)
async def learn(
    payload: LearnRequest,
):

    try:

        return LearnResponse(
            recommendations=(
                get_learning_recommendations(
                    payload.topic,
                    payload.level,
                    payload.hours_per_week,
                )
            )
        )

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc),
        ) from exc 