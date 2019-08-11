import tweepy
import logging
from os import environ

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
