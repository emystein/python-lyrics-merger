from peewee import *
import os
from urllib.parse import urlparse, uses_netloc
import psycopg2


# if 'DATABASE_URL' in os.environ:
#     uses_netloc.append('postgres')
#     url = urlparse(os.environ["DATABASE_URL"])
#     database = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
# else:
#     database = SqliteDatabase(':memory:')

database_proxy = DatabaseProxy()
# database_proxy.initialize(database)


class StreamCursor(Model):
    key = CharField(primary_key=True)
    position = BigIntegerField(default=1)

    class Meta:
        database = database_proxy
