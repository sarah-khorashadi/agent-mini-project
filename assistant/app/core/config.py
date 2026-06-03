import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    LLM_MODEL = os.getenv("LLM_MODEL")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_URL")
    QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION")


settings = Settings()