from peewee import *


database_proxy = DatabaseProxy()


class StreamCursor(Model):
    key = CharField(primary_key=True)
    position = BigIntegerField(default=1)

    class Meta:
        database = database_proxy
