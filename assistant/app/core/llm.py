# from langchain_ollama import ChatOllama
from langchain_openrouter import ChatOpenRouter

from app.core.config import settings

# chat_model = ChatOllama(
#     model=settings.LLM_MODEL,
#     base_url=settings.OLLAMA_HOST,
#     temperature=0.2,
# )

chat_model = ChatOpenRouter(
    model=settings.LLM_MODEL,
    temperature=0.2,
    max_retries=5
)
