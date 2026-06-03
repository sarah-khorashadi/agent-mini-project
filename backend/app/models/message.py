from sqlalchemy import Integer, Column, String, DateTime, Boolean, ForeignKey
from datetime import datetime
from app.core.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(String, ForeignKey("users.user_id"))

    user_message = Column(String)
    assistant_reply = Column(String)

    intent = Column(String, nullable=True)
    needs_human_support = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)