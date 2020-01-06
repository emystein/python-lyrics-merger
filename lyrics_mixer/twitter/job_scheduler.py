import logging
import schedule
import time
import jobs
import os
from urllib.parse import urlparse, uses_netloc
from peewee import *
import psycopg2
from streams.persistence import StreamCursor
from lyrics_mixer.artists_parser import ArtistsParser
from lyrics_mixer.dispatcher import Dispatcher
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient
from twitter.twitter import TwitterApi, TweetReplyFactory
from reply_strategies import MixLyricsReplyStrategy

logging.basicConfig(level=logging.INFO)

if 'DATABASE_URL' in os.environ:
    uses_netloc.append('postgres')
    url = urlparse(os.environ["DATABASE_URL"])
    database = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
else:
    database = SqliteDatabase(':memory:')

database.bind([StreamCursor])

twitter_api = TwitterApi()

dispatcher = Dispatcher(WikiaLyricsApiClient(), LineInterleaveLyricsMix())

schedule.every().minute.do(jobs.reply_to_mentions, twitter_api = twitter_api, tweet_reply_factory = TweetReplyFactory(ArtistsParser(), MixLyricsReplyStrategy(dispatcher)))
schedule.every(4).hours.do(jobs.tweet_random_lyrics, twitter_api = twitter_api, dispatcher = dispatcher).run()
    
def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
