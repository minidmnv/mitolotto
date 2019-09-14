class User(object):
    def __init__(self, data):
        self.username = data.json['username']
        self.password = data.json['password']
        self.image = data.json['image']


class AuthorizeResponse(object):
    def __init__(self, authorized: str, details: str):
        self.authorized = authorized
        self.details = details
