from peewee import *
import os


database_proxy = DatabaseProxy()


class StreamCursor(Model):
    key = CharField(primary_key=True)
    position = BigIntegerField()

    class Meta:
        database = database_proxy


if 'HEROKU' in os.environ:
    import urlparse, psycopg2
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    database = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
else:
    database = SqliteDatabase(':memory:')


database_proxy.initialize(database)