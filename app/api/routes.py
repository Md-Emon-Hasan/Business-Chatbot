from fastapi import APIRouter
from graph.builder import build_graph

router = APIRouter()
app_graph = build_graph()

@router.post("/chat")
def chat(payload: dict):
    state = {
        "message": payload["message"],
        "conversation_history": payload.get("conversation_history", [])
    }

    result = app_graph.invoke(state)

    return {
        "answer": result["response"],
        "history": result["conversation_history"]
    }
