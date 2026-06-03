import httpx

from sqlalchemy.orm import Session

from app.schemas.message import MessageRequest
from app.schemas.message import MessageResponse

from app.models.user import User
from app.models.message import Message

from fastapi import HTTPException, status

# from app.services.agent.agent import Agent

class MessageController:

    @staticmethod
    def process_message(db: Session, payload: MessageRequest):
        
        # validate that user_id is not empty or only whitespace
        if not payload.user_id or not payload.user_id.strip():
            raise HTTPException(
                status_code=400,
                detail="user_id cannot be empty"
            )

        # check if user exists in the database
        user = db.query(User).filter(User.user_id == payload.user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User '{payload.user_id}' does not exist"
            )

        # validate that message field is not empty or only whitespace
        if not payload.message or not payload.message.strip():
            raise HTTPException(
                status_code=400,
                detail="message cannot be empty"
            )

        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.post(
                    "http://rastad-assistant:8000/api/ask",
                    json={
                        "question": payload.message,
                        "user_id": payload.user_id
                    }
                )

            if response.status_code != 200:
                raise HTTPException(
                    status_code=500,
                    detail="Assistant service failed"
                )

            data = response.json()

            reply = data.get("reply", "")
            intent = data.get("intent", "unknown")
            user_segment = data.get("user_segment", "unknown")
            needs_human_support = data.get("needs_human_support", False)

        except httpx.RequestError as e:
            raise HTTPException(
                status_code=503,
                detail=f"Assistant service unavailable: {str(e)}"
            )
        
        message = Message(
            user_id=user.user_id,
            user_message=payload.message,
            assistant_reply=reply,
            intent=intent,
            needs_human_support=needs_human_support
        )

        db.add(message)
        db.commit()
        db.refresh(message)

        return MessageResponse(
            reply=reply,
            intent=intent,
            user_segment=user_segment,
            needs_human_support=needs_human_support
        )