from fastapi import FastAPI

from app.api.api_router import api_router
from app.core.database import Base, engine
from app.core.seed import seed_users
# Base.metadata.create_all(bind=engine)

from app.schemas.base import APIResponse

app = FastAPI(
    title="Rastad Chat Service"
)

@app.get("/health")
def health():
    return {"status": "ok"}
    
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    seed_users()

app.include_router(api_router)
APIResponse.model_rebuild()