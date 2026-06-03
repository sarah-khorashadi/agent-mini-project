from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.base import APIResponse
from app.schemas.message import MessageRequest, MessageResponse

from app.controllers.message_controller import MessageController

router = APIRouter(tags=["Messages"])


@router.post("/message", response_model=APIResponse[MessageResponse])
def send_message(
    payload: MessageRequest,
    db: Session = Depends(get_db)
):
    result = MessageController.process_message(db, payload)
    return APIResponse(
        result=result,
        status_code=200
    )