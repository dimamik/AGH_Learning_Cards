from app import UserContext
from app.http.errors import BadRequestException


class UserCreationRequest:
    def __init__(self, data_dict: dict):
        try:
            print(data_dict)
            self.user_name = data_dict['username']
            self.user_email = data_dict['email']
            self.user_password = data_dict['password']
        except (TypeError, KeyError):
            raise BadRequestException('Cannot deserialize UserCreationRequest')


class UserLoginRequest:
    def __init__(self, data_dict: dict):
        try:
            self.user_email = data_dict['email']
            self.user_password = data_dict['password']
        except (TypeError, KeyError):
            raise BadRequestException('Cannot deserialize UserLoginRequest')


class UserResponse:
    def __init__(self, user_context: UserContext):
        self.user_name = user_context.instance.userName

    def to_dict(self):
        return {
            'username': self.user_name
        }
