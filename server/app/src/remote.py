from db import db
from exceptions import WrongUsernameOrPassword

def authorize(password, password_from_mock_remote_api):
    if password == password_from_mock_remote_api:
        return True
    else:
        raise WrongUsernameOrPassword('Wrong username or password')


def get_user_from_mock_remote_api(username: str):
    if username in db.users:
        return db.users[username]
    else:
        raise WrongUsernameOrPassword('Wrong username or password')
