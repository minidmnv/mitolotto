class User(object):

    def __init__(self, username, password, image):
        self.username = username
        self.password = password
        self.image = image


class AuthorizeResponse(object):
    def __init__(self, authorized: str, details: str):
        self.authorized = authorized
        self.details = details
