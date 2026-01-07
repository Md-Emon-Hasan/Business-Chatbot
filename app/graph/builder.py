from langgraph.graph import StateGraph, END
from graph.state import ChatState
from graph.nodes import (
    input_node,
    intent_objective_agent,
    rag_agent,
    persona_agent,
    response_agent
)

def build_graph():
    graph = StateGraph(ChatState)

    graph.add_node("input", input_node)
    graph.add_node("intent", intent_objective_agent)
    graph.add_node("rag", rag_agent)
    graph.add_node("persona", persona_agent)
    graph.add_node("response", response_agent)

    graph.set_entry_point("input")
    graph.add_edge("input", "intent")
    graph.add_edge("intent", "rag")
    graph.add_edge("rag", "persona")
    graph.add_edge("persona", "response")
    graph.add_edge("response", END)

    return graph.compile()
