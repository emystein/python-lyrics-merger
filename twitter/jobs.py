import logging
import time
import twitter
from twitter import MentionsReplyCursor, MixLyricsReplyStrategy

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    twitter_api.update_status(mixed_lyrics) 


def reply_to_mentions(twitter_api, reply_strategy):
    cursor = MentionsReplyCursor()
    logger.info(f"Replying to mentions since: {cursor.position}")
    mentions = twitter_api.mentions_since(cursor.position)
    for mention in mentions:
        mention.reply_with(reply_strategy) 
        cursor.point_to(mention)