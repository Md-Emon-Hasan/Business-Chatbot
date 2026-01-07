from core.llm import get_llm
from vectorstore.chroma_store import get_retriever

llm = get_llm()
retriever = get_retriever()

def input_node(state):
    return {
        "message": state["message"],
        "conversation_history": state.get("conversation_history", [])
    }

def intent_objective_agent(state):
    history = "\n".join(
        f"User: {h['user']}\nAssistant: {h['assistant']}"
        for h in state.get("conversation_history", [])[-3:]
    )

    prompt = f"""
You are an intent & decision-objective classifier.

Previous conversation:
{history}

Current question:
{state['message']}

Return JSON:
{{
  "primary_intent": "...",
  "decision_objective": "...",
  "topics": ["pricing", "integration", "services", "tech"],
  "confidence": 0.0
}}
"""
    res = llm.invoke(prompt)
    return {"intent_objective": res.content}

# def rag_agent(state):
#     docs = retriever.invoke(state["message"])
#     context = "\n".join(d.page_content for d in docs)
#     return {"rag_context": context}

def rag_agent(state):
    retrieved_docs = retriever.invoke(state["message"])

    seen = set()
    unique_chunks = []

    for doc in retrieved_docs:
        content = doc.page_content.strip()
        if content not in seen:
            seen.add(content)
            unique_chunks.append(content)

    context = "\n".join(unique_chunks)
    return {"rag_context": context}


def persona_agent(state):
    prompt = f"""
Based on intent below, choose persona.

{state['intent_objective']}

Return JSON:
{{
  "primary_persona": "sales | tech | general",
  "secondary_personas": []
}}
"""
    res = llm.invoke(prompt)
    return {"persona_decision": res.content}

def response_agent(state):
    history = "\n".join(
        f"User: {h['user']}\nAssistant: {h['assistant']}"
        for h in state.get("conversation_history", [])[-3:]
    )

    prompt = f"""
You are a business AI assistant.

Rules:
- Use ONLY provided context
- Be honest if info missing

Previous conversation:
{history}

Context:
{state['rag_context']}

Persona:
{state['persona_decision']}

Question:
{state['message']}
"""
    res = llm.invoke(prompt)

    history_updated = state.get("conversation_history", []).copy()
    history_updated.append({
        "user": state["message"],
        "assistant": res.content
    })

    return {
        "response": res.content,
        "conversation_history": history_updated
    }
