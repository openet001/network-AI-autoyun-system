from fastapi import APIRouter, Query
from app.schemas import AIRequest, AIResponse
from app.services.ai import ask_ai

router = APIRouter()

@router.post("/ask", response_model=AIResponse)
def ai_ask(request: AIRequest, model: str = Query("openai", enum=["openai", "deepseek", "doubot"])):
    answer = ask_ai(request.question, model)
    return AIResponse(answer=answer)