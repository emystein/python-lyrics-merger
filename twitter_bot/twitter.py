import tweepy
import logging
from os import environ

logger = logging.getLogger()


def create_tweepy_api():
    auth = tweepy.OAuthHandler(
        environ['LYRICS_MIXER_TWITTER_CONSUMER_KEY'], environ['LYRICS_MIXER_TWITTER_CONSUMER_SECRET'])
    auth.set_access_token(
        environ['LYRICS_MIXER_TWITTER_ACCESS_TOKEN'], environ['LYRICS_MIXER_TWITTER_ACCESS_TOKEN_SECRET'])

    return tweepy.API(auth)


class TwitterApi:
    MAX_TWEET_LENGTH = 280

    def __init__(self, api):
        self.api = api

    def mentions_since(self, since_id):
        tweets = tweepy.Cursor(self.api.mentions_timeline, since_id).items()
        return self.mentions(tweets)

    def mentions(self, tweets):
        return filter(lambda tweet: tweet.in_reply_to_status_id is None, tweets)

    def update_status(self, text):
        self.api.update_status(text[:self.MAX_TWEET_LENGTH])

    def reply_tweet_with(self, origin_tweet, reply_text):
        self.api.update_status(
            status=reply_text[:self.MAX_TWEET_LENGTH], in_reply_to_status_id=origin_tweet.id)


class MentionHistory:
    def __init__(self, twitter_api, reply_cursor):
        self.twitter_api = twitter_api
        self.reply_cursor = reply_cursor

    def since_last_persisted(self):
        return self.twitter_api.mentions_since(self.reply_cursor.position)

    def add(self, mention):
        self.reply_cursor.point_to(mention)


class Composer:
    def __init__(self, twitter_api, tweet_parser, lyrics_mixer):
        self.twitter_api = twitter_api
        self.tweet_parser = tweet_parser
        self.lyrics_mixer = lyrics_mixer

    def tweet(self, mixed_lyrics):
        logger.info(f"Tweeting Mixed Lyrics")

        if mixed_lyrics.has_content():
            try:
                self.twitter_api.update_status(str(mixed_lyrics))
            except:
                logger.error('Skipping tweet.', exc_info=True)

    def reply(self, tweet):
        logger.info(f"Replying to Tweet with ID: {tweet.id} and Text: {tweet.text}")
        parsed = self.tweet_parser.parse(tweet.text)
        lyrics = parsed.mix_using(self.lyrics_mixer)
        if lyrics.has_content():
            self.twitter_api.reply_tweet_with(tweet, str(lyrics))
