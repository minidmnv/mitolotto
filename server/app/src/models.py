class User(object):
    def __init__(self, data):
        self.username = data.json['username']
        self.password = data.json['password']
        self.image = data.json['image']
        
    def __init__(self, username: str, password: str, image: str):
        self.username = username
        self.password = password
        self.image = image


class AuthorizeResponse(object):
    def __init__(self, authorized: str, details: str):
        self.authorized = authorized
        self.details = details
