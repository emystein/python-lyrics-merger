import logging
from streams.orm import StreamCursor


logger = logging.getLogger()


class MentionsReplyCursor(object):
    def __init__(self):
        self.cursor, self.created = StreamCursor.get_or_create(key = 'twitter')
        logger.info(f"Mentions reply cursor at position: {self.cursor.position}")

    @property
    def position(self):
        return self.cursor.position

    @position.setter
    def position(self, position):
        self.cursor.position = position

    def save(self):
        self.cursor.save()

    def point_to(self, mention):
        self.position = mention.id
        self.save()