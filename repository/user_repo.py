import bcrypt
from sqlalchemy.orm import Session
from db.models.user import User


class UserRepo(object):
    def __init__(self, db: Session):
        self.db = db

    def save(self, user_obj: User) -> User:
        hashed_password = bcrypt.hashpw(user_obj.password.encode('utf-8'), bcrypt.gensalt())
        user_obj.password = hashed_password
        self.db.add(user_obj)
        self.db.commit()
        self.db.refresh(user_obj)
        return user_obj

    def find_all(self):
        users = self.db.query(User).all()
        return users

    def find_by_email(self, email: str) -> User:
        user_obj = self.db.query(User).filter(User.email == email).first()
        return user_obj
