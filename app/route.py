from fastapi import APIRouter
from app.model import RequestState
from agents.ai_agents import get_response_from_ai_agent

router = APIRouter()

ALLOWED_MODELS = {"llama-3.3-70b-versatile"}

@router.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODELS:
        return {"error": "Unsupported model"}

    query = request.messages[-1] if request.messages else ""
    response = get_response_from_ai_agent(
        llm_id= request.model_name,
        query = query,
        web_search_allowed = request.allow_search,
        system_prompt = request.system_prompt,
        provider=request.model_provider
    )
    return response