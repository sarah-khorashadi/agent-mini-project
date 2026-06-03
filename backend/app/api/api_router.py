from fastapi import APIRouter

from app.api.message_routes import router as message_router
from app.api.user_routes import router as user_router

api_router = APIRouter()

api_router.include_router(message_router)
api_router.include_router(user_router)