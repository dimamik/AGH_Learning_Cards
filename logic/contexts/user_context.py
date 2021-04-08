from database.models.database_init import db
from database.models.main_models import User
from logic.encryption.password import verify_password, create_bcrypt_hash


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
    def log_user_in(username: str, password: str) -> bool:
        if UserContext.get_user_instance_by_username(username).log_in(password):
            return True
        return False

    @staticmethod
    def add_new_user(username: str, password: str):
        if not UserContext.get_user_instance_by_username(username):
            user_instance = UserContext()
            user_instance.set_user_name(username)
            user_instance.set_password(password)
