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
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api


class TwitterApi(object):
    def __init__(self):
        self.twitter_api = create_tweepy_api()

    def mentions_since(self, since_id):
        tweets = tweepy.Cursor(
            self.twitter_api.mentions_timeline, since_id).items()
        mentions = filter(self.is_not_reply, tweets)
        return map(lambda mention: Tweet(self, mention), mentions)

    def is_not_reply(self, tweet):
        return tweet.in_reply_to_status_id is None

    def update_status(self, tweet):
        self.twitter_api.update_status(tweet[:MAX_TWEET_LENGTH])

    def reply_tweet_with(self, tweet, reply_text):
        self.twitter_api.update_status(
            status=reply_text[:MAX_TWEET_LENGTH], in_reply_to_status_id=tweet.id)


class Tweet(object):
    def __init__(self, twitter_api, tweet):
        self.twitter_api = twitter_api
        self.tweet = tweet
        self.user = tweet.user
        self.text = tweet.text

    def reply_with(self, reply_text):
        self.twitter_api.reply_tweet_with(self.tweet, reply_text)

    def __str__(self):
        return f"Author: @{self.user.name}, Text: {self.text}"


class TweetReplyFactory:
    def __init__(self, input_parser, composer):
        self.input_parser = input_parser
        self.composer = composer

    def create_from_many(self, tweets):
        return map(lambda tweet: self.create_from(tweet), tweets)

    def create_from(self, tweet):
        return TweetReply(tweet).parse_with(self.input_parser).write_with(self.composer)


class TweetReply:
    def __init__(self, tweet):
        self.tweet = tweet
        self.id = tweet.id

    def parse_with(self, tweet_parser):
        self.parsed_data_from_tweet = tweet_parser.parse(self.tweet.text)
        return self

    def write_with(self, composer):
        self.text = composer.write_reply(self.tweet, self.parsed_data_from_tweet)
        return self

    def send(self):
        logger.info(f"Replying to tweet: {self.tweet}")
        self.tweet.reply_with(self.text)
