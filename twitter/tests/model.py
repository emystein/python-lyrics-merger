class User:
    def __init__(self, name):
        self.name = name


class Tweet:
    def __init__(self, username, text):
        self.author = User(username)
        self.text = text
