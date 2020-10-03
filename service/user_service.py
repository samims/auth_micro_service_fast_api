import bcrypt

from repository.user_repo import UserRepo
from db.models.user import User


class UserService(object):
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def signup(self, user_obj: User):
        # TODO: add validator
        if self.user_repo.find_by_email(user_obj.email):
            # return {"success": False, "message": " email already exists"}
            raise Exception(f"user with email '{user_obj.email}' already exists")
        user = self.user_repo.save(user_obj)
        return {"user": user}

    def login(self, user_obj: User):
        db_user = self.user_repo.find_by_email(email=user_obj.email)
        valid_credential = bcrypt.checkpw(user_obj.password.encode("utf-8"), db_user.password.encode("utf-8"))
        if valid_credential:
            pass
        pass
