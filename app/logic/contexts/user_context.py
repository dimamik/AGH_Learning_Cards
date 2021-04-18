from typing import Optional

from app.database.models.database_init import db
from app.database.models.main_models import User
from app.logic.encryption.password import verify_password, create_bcrypt_hash


class UserContext:
    def __init__(self, user=None):
        super(UserContext, self).__init__()
        if user is None:
            user = User()
            db.session.add(user)
            db.session.commit()
        self.user = user

    def set_user_name(self, username):
        self.user.userName = username
        db.session.commit()

    def set_user_info(self, info: str):
        self.user.userInfo = info
        db.session.commit()

    def log_in(self, password):
        return verify_password(password, self.user.userPasswordHash)

    def change_password(self, old_password, new_password):
        if self.log_in(old_password):
            self.set_password(new_password)
            return True
        return False

    def set_password(self, new_password):
        self.user.userPasswordHash = create_bcrypt_hash(new_password)
        db.session.commit()

    @staticmethod
    def get_user_instance_by_id(uid: int):
        user = db.session.query(User).filter(User.userID == uid).first()
        return UserContext(user)

    @staticmethod
    def get_user_instance_by_username(username):
        user = db.session.query(User).filter(User.userName == username).first()
        return UserContext(user) if user else False

    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        user = db.session.query(User).filter(User.userEmail == email).first()
        return user if user else None

    @staticmethod
    def get_user_by_name_or_email(name: str, email: str) -> Optional[User]:
        user = db.session.query(User).filter(User.userName == name or User.userEmail == email).first()
        return user if user else None

    @staticmethod
    def log_user_in(username: str, password: str) -> bool:
        if UserContext.get_user_instance_by_username(username).log_in(password):
            return True
        return False

    @staticmethod
    def add_new_user(user: User):
        db.session.add(user)
        db.session.commit()
