class User(object):
    def __init__(self, data):
        self.username = data.json['username']
        self.password = data.json['password']
        self.image = data.json['image']