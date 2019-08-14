import psycopg2
from lyrics_mixer.orm import *
from twitter.jobs import MentionsReplyCursor

database_proxy.connect()
database_proxy.create_tables([StreamCursor], safe=True)
database_proxy.create_tables([MentionsReplyCursor], safe=True)