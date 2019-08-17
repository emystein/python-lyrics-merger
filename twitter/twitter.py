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
        self.position = max(self.position, mention.id)
        self.save()


class MixLyricsReplyStrategy(object):
    def __init__(self, input_parser, lyrics_mixer):
        self.input_parser = input_parser
        self.lyrics_mixer = lyrics_mixer
    
    def get_reply_for(self, tweet):
        logger.info(f"Mixing lyrics requested by: {tweet.user.name}, using input: '{tweet.text}'")
        parsed = self.input_parser.parse(tweet.text)
        mixed_lyrics = self.lyrics_mixer.mix_random_lyrics_by_artists(parsed.artist1, parsed.artist2)
        return f"@{tweet.user.name} {mixed_lyrics}"