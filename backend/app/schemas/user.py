from pydantic import BaseModel
from datetime import datetime

class UserResponse(BaseModel):
    user_id: str
    name : str
    segment: str
    created_at: datetime
    last_seen_at: datetime | None = None

    class Config:
        from_attributes = True