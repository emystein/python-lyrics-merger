import tweepy
import logging
from os import environ
from peewee import *


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
    api.verify_credentials()

    logger.info("API created")

    return api


def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    twitter_api.update_status(str(mixed_lyrics))


def reply_to_mentions(twitter_api, tweet_parser, lyrics_mixer):
    reply_cursor = MentionsReplyCursor()

    logger.info(f"Mentions reply cursor at position: {reply_cursor.position}")

    mentions = twitter_api.mentions_since(reply_cursor.position)

    for mention in mentions:
        reply = TweetReply(mention).parse_with(tweet_parser).compose_reply(lyrics_mixer)
        reply.send()
        reply_cursor.point_to(reply)


class TwitterApi(object):
    MAX_TWEET_LENGTH = 280

    def __init__(self):
        self.api = create_tweepy_api()

    def mentions_since(self, since_id):
        tweets = tweepy.Cursor(self.api.mentions_timeline, since_id).items()
        return self.mentions(tweets)

    def mentions(self, tweets):
        mentions = filter(lambda tweet: tweet.in_reply_to_status_id is None, tweets)
        return map(lambda mention: Tweet(self, mention), mentions)

    def update_status(self, tweet):
        self.api.update_status(tweet[self.MAX_TWEET_LENGTH])

    def reply_tweet_with(self, tweet, reply_text):
        self.api.update_status(status=reply_text[self.MAX_TWEET_LENGTH],
                               in_reply_to_status_id=tweet.id)


class Tweet:
    def __init__(self, twitter_api, tweet):
        self.api = twitter_api
        self.tweet = tweet
        self.author = tweet.user
        self.text = tweet.text

    def reply_with(self, reply_text):
        self.api.reply_tweet_with(self.tweet, reply_text)

    def __str__(self):
        return f"Author: @{self.author.name}, Text: {self.text}"


class TweetReply:
    def __init__(self, tweet):
        self.tweet = tweet
        self.id = tweet.id

    def parse_with(self, tweet_parser):
        return ParsedTweet(self.tweet, tweet_parser.parse(self.tweet.text))


class ParsedTweet:
    def __init__(self, tweet, parsed_data_from_tweet):
        self.tweet = tweet
        self.parsed_data_from_tweet = parsed_data_from_tweet

    def compose_reply(self, lyrics_mixer):
        lyrics = self.parsed_data_from_tweet.mix_using(lyrics_mixer)
        return ComposedReply(self.tweet, lyrics)


class ComposedReply:
    def __init__(self, origin_tweet, reply_text):
        self.origin_tweet = origin_tweet
        self.id = origin_tweet.id
        self.text = f"@{origin_tweet.author.name} {reply_text}"

    def send(self):
        logger.info(f"Replying to tweet: {self.origin_tweet}")
        self.origin_tweet.reply_with(self.text)

    def __eq__(self, other):
        return self.origin_tweet == other.origin_tweet and self.text == other.text


class StreamCursor(Model):
    key = CharField(primary_key=True)
    position = BigIntegerField(default=1)


class MentionsReplyCursor:
    def __init__(self):
        self.cursor, self.created = StreamCursor.get_or_create(key='twitter')

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
