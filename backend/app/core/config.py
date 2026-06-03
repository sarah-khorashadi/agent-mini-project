import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    ASSISTANT_URL = os.getenv("ASSISTANT_URL")


settings = Settings()