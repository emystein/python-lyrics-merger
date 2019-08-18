import tweepy
import logging
from os import environ


MAX_TWEET_LENGTH = 280

logger = logging.getLogger()


def create_tweepy_api():
    CONSUMER_KEY = environ['TWITTER_CONSUMER_KEY']
    CONSUMER_SECRET = environ['TWITTER_CONSUMER_SECRET']
    ACCESS_TOKEN = environ['TWITTER_ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = environ['TWITTER_ACCESS_TOKEN_SECRET']

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


class TwitterApiWrapper(object):
    def __init__(self):
        tweepy_api = create_tweepy_api()
        self.twitter_api = tweepy_api

    def mentions_since(self, since_id):
        tweets = tweepy.Cursor(
            self.twitter_api.mentions_timeline, since_id).items()
        mentions = filter(self.is_not_reply, tweets)
        return map(lambda mention: TweetWrapper(self, mention), mentions)

    def is_not_reply(self, tweet):
        return tweet.in_reply_to_status_id is None

    def update_status(self, tweet):
        self.twitter_api.update_status(
            tweet[:twitter.twitter.MAX_TWEET_LENGTH])

    def reply_tweet_with(self, tweet, reply_text):
        self.twitter_api.update_status(
            status=reply_text[:twitter.twitter.MAX_TWEET_LENGTH], in_reply_to_status_id=tweet.id)


class TweetWrapper(object):
    def __init__(self, twitter_api_wrapper, tweet):
        self.twitter_api_wrapper = twitter_api_wrapper
        self.tweet = tweet
        self.id = tweet.id
        self.user = tweet.user
        self.text = tweet.text

    def reply_using_strategy(self, reply_strategy):
        reply_text = reply_strategy.get_reply_for(self)
        self.reply_with(reply_text)

    def reply_with(self, reply_text):
        self.twitter_api_wrapper.reply_tweet_with(self.tweet, reply_text)