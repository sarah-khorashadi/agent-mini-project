from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.controllers.user_controller import UserController

from app.schemas.base import APIResponse
from app.schemas.user import UserResponse
from app.schemas.message import MessageHistoryResponse


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=APIResponse[list[UserResponse]])
def get_users(db: Session = Depends(get_db)):
    users = UserController.get_users(db)
    return APIResponse(result=users, status_code=200)
    
    

@router.get("/{user_id}/messages", response_model=APIResponse[list[MessageHistoryResponse]])
def get_user_messages(user_id: str, db: Session = Depends(get_db)):
    messages = UserController.get_user_messages(db, user_id)
    return APIResponse(result= messages, status_code=200)