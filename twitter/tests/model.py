class User:
    def __init__(self, name):
        self.name = name


class FakeTweet:
    def __init__(self, id, username, text):
        self.id = id
        self.user = User(username)
        self.text = text
