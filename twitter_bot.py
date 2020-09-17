import logging
import schedule
import time
import os
from urllib.parse import urlparse, uses_netloc
from peewee import *
import psycopg2
from lyrics_mixer.lyrics_data_source import LyricsDataSource
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser
import twitter_bot.jobs
import twitter_bot.persistence
from twitter_bot.persistence import StreamCursor, MentionsReplyCursor
import twitter_bot.twitter
from twitter_bot.twitter import TwitterApi

logging.basicConfig(level=logging.INFO)

if 'DATABASE_URL' in os.environ:
    uses_netloc.append('postgres')
    url = urlparse(os.environ["DATABASE_URL"])
    database = PostgresqlDatabase(
        database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port, autoconnect=False)
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

# advance reply cursor to a mention already replied
cursor = MentionsReplyCursor()
if cursor.position < 1305235263355052032:
    cursor.position = 1305235263355052032
    cursor.save()

api = twitter_bot.twitter.create_tweepy_api()

twitter_api = TwitterApi(api)

lyrics_mixer = LyricsMixer(
    LyricsDataSource(), LineInterleaveLyricsMix())

schedule.every().minute.do(twitter_bot.jobs.reply_to_mentions, twitter_api=twitter_api,
                           tweet_parser=SongTitlesParser(SongTitlesSplitter()),
                           lyrics_mixer=lyrics_mixer)

schedule.every(4).hours.do(twitter_bot.jobs.tweet_random_lyrics,
                           twitter_api=twitter_api,
                           lyrics_mixer=lyrics_mixer).run()


def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
