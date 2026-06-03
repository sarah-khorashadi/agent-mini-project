from app.core.llm import chat_model
from app.workflows.state import RAGState

from langchain_core.prompts import ChatPromptTemplate


prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a precise AI assistant. Your segment is {segment} and your intent is {intent}."),
    ("user", "Context:\n{context}\n\nQuestion:\n{question}")
])

def generate(state: RAGState) -> dict:
    context = "\n\n".join(d.page_content for d in state.get("context", []))

    prompt = prompt_template.invoke({
            "segment": state.get("segment", "unknown"),
            "intent": state.get("intent", "general"),
            "context": context if context else "No relevant context found.",
            "question": state["question"]
        })

    res = chat_model.invoke(prompt)

    return {"answer": res.content}