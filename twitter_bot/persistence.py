import logging
import os
import time
from urllib.parse import urlparse, uses_netloc

from peewee import *

logger = logging.getLogger()


def connect_to_database():
    if 'DATABASE_URL' in os.environ:
        uses_netloc.append('postgres')
        url = urlparse(os.environ["DATABASE_URL"])
        database = PostgresqlDatabase(
            database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port,
            autoconnect=False)
    else:
        database = SqliteDatabase(':memory:')

    while database.is_closed():
        try:
            database.connect()
        except:
            pass
        time.sleep(1)

    database.bind([StreamCursor])
    database.create_tables([StreamCursor], safe=True)


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
