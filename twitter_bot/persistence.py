import logging
from peewee import *


logger = logging.getLogger()


class StreamCursor(Model):
    key = CharField(primary_key=True)
    position = BigIntegerField(default=1)


class MentionsReplyCursor:
    def __init__(self):
        self.cursor, self.created = StreamCursor.get_or_create(key='twitter')
        logger.info(f"Mentions reply cursor at position: {self.position}")


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