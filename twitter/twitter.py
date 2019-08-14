import tweepy
import logging
from os import environ
from lyrics_mixer.orm import StreamCursor

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

    @property
    def position(self):
        return self.cursor.position

    @position.setter
    def position(self, position):
        self.cursor.position = position

    def save(self):
        self.cursor.save()

    def update_from_mentions(self, mentions):
        new_since_id = mentions[-1].id if len(mentions) > 0 else 1
        self.cursor.position = max(self.cursor.position, new_since_id)
        self.cursor.save()