from db.config import get_db
from .user_service import UserService
from repository.user_repo import UserRepo


def get_user_service() -> UserService:
    db = get_db()
    user_repo = UserRepo(db)
    user_svc = UserService(user_repo=user_repo)
    return user_svc


user_service = get_user_service()
