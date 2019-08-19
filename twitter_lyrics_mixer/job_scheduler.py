import logging
import schedule
import time
import jobs
from lyrics_mixer.artists_parser import ArtistsParser
from lyrics_mixer.lyrics_mixer import LyricsMixer
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient
from twitter.twitter import TwitterApi, TweetReplyFactory
from reply_strategies import MixLyricsReplyStrategy
import streams.persistence


logging.basicConfig(level=logging.INFO)

twitter_api = TwitterApi()

import os
from urllib.parse import urlparse, uses_netloc
import psycopg2


if 'DATABASE_URL' in os.environ:
    uses_netloc.append('postgres')
    url = urlparse(os.environ["DATABASE_URL"])
    database = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
else:
    database = SqliteDatabase(':memory:')

database_proxy.initialize(database)

lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())

schedule.every().minute.do(jobs.reply_to_mentions, twitter_api = twitter_api, tweet_reply_factory = TweetReplyFactory(ArtistsParser(), MixLyricsReplyStrategy(lyrics_mixer)))
schedule.every(4).hours.do(jobs.tweet_random_lyrics, twitter_api = twitter_api, lyrics_mixer = lyrics_mixer).run()
    
def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
