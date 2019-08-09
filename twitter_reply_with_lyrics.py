import tweepy
import logging
import time
import twitter
from lyrics_mixer.lyrics_mixer_app import LyricsMixerApp 
from lyrics_mixer.orm import StreamCursor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def reply_to_mentions(twitter_api):
    cursor, created = StreamCursor.get_or_create(key = 'tweeter')
    reply_strategy = MixLyricsReplyStrategy()
    cursor.position = check_mentions(twitter_api, cursor.position, reply_strategy)
    cursor.save()


class MixLyricsReplyStrategy(object):
    def __init__(self):
        self.mixer = LyricsMixerApp() 
    
    def get_reply_for(self, tweet):
        logger.info(f"Mixing lyrics requested by: {tweet.user.name}, using input: '{tweet.text}'")
        mixed_lyrics = str(self.mixer.mix_lyrics_parsing_input(tweet.text))
        return f"@{tweet.user.name} {mixed_lyrics}"


def check_mentions(api, since_id, reply_strategy):
    logger.info(f"Checking mentions since: {since_id}")

    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        reply_text = reply_strategy.get_reply_for(tweet)
        reply_tweet_with(api, tweet, reply_text)
    return new_since_id


def reply_tweet_with(api, tweet, reply_text):
    api.update_status(status = reply_text[:twitter.MAX_TWEET_LENGTH], in_reply_to_status_id = tweet.id)
