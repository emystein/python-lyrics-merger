class User:
    def __init__(self, name):
        self.name = name


class TweetForTest:
    def __init__(self, username, text):
        self.user = User(username)
        self.text = text
