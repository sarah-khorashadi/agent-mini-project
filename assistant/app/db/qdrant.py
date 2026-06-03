from langchain_qdrant import QdrantVectorStore
# from langchain_ollama import OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import settings

SEARCH_KWARGS = 4

def get_vectorstore():
    # return QdrantVectorStore.from_existing_collection(
    #     embedding=OllamaEmbeddings(model=settings.EMBEDDING_MODEL),
    #     collection_name=settings.QDRANT_COLLECTION,
    #     url=settings.QDRANT_URL,
    # )
    return QdrantVectorStore.from_existing_collection(
        embedding=HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL),
        collection_name=settings.QDRANT_COLLECTION,
        url=settings.QDRANT_URL,
    )


def get_retriever():
    return get_vectorstore().as_retriever(search_kwargs={"k": SEARCH_KWARGS})