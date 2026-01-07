from typing import TypedDict, List

class ChatState(TypedDict):
    message: str
    intent_objective: str
    rag_context: str
    persona_decision: str
    response: str
    conversation_history: List[dict]
