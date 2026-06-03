from pydantic import BaseModel
from datetime import datetime


class MessageRequest(BaseModel):
    user_id: str
    name: str
    message: str


class MessageResponse(BaseModel):
    reply: str
    intent: str | None = None
    user_segment: str | None = None
    needs_human_support: bool

class MessageHistoryResponse(BaseModel):
    id: int
    user_id: str
    user_message: str
    assistant_reply: str
    intent: str | None
    needs_human_support: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }