import tweepy
import logging
from os import environ
from streams.orm import StreamCursor

MAX_TWEET_LENGTH = 280

logger = logging.getLogger()


def create_api():
    CONSUMER_KEY = environ['LYRICSMIXER_TWITTER_CONSUMER_KEY']
    CONSUMER_SECRET = environ['LYRICSMIXER_TWITTER_CONSUMER_SECRET']
    ACCESS_TOKEN = environ['LYRICSMIXER_TWITTER_ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = environ['LYRICSMIXER_TWITTER_ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api


class MentionsReplyCursor(object):
    def __init__(self):
        self.cursor, self.created = StreamCursor.get_or_create(key = 'twitter')
        logger.info(f"Mentions reply cursor at position: {self.cursor.position}")

    @property
    def position(self):
        return self.cursor.position

    @position.setter
    def position(self, position):
        self.cursor.position = position

    def save(self):
        self.cursor.save()

    def point_to(self, mention):
        self.position = mention.id
        self.save()