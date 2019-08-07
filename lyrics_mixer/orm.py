from peewee import *
import os


database_proxy = DatabaseProxy()


class StreamCursor(Model):
    key = CharField(primary_key=True)
    position = BigIntegerField()

    class Meta:
        database = database_proxy


if 'IS_PRODUCTION' in os.environ:
    database = PostgresqlDatabase('lyricsmixer')
else:
    database = SqliteDatabase(':memory:')


database_proxy.initialize(database)