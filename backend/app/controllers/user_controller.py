from sqlalchemy.orm import Session

from app.models.user import User
from app.models.message import Message

class UserController:

    @staticmethod
    def get_users(db: Session):
        return db.query(User).all()


    @staticmethod
    def get_user_messages(db: Session, user_id: str):
        print(user_id)
        return db.query(Message).filter(Message.user_id == user_id).order_by(Message.created_at.desc()).all()