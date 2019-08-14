import psycopg2
from lyrics_mixer.orm import *

database_proxy.connect()
database_proxy.create_tables([StreamCursor], safe=True)