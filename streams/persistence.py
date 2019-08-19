from peewee import *


class StreamCursor(Model):
    key = CharField(primary_key=True)
    position = BigIntegerField(default=1)
