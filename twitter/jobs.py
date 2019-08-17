import time
import twitter
from twitter import MentionsReplyCursor, MixLyricsReplyStrategy


def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    twitter_api.update_status(mixed_lyrics) 


def reply_to_mentions(twitter_api, reply_strategy):
    cursor = MentionsReplyCursor()
    mentions = twitter_api.mentions_since(cursor.position)
    for mention in mentions:
        mention.reply_using_strategy(reply_strategy) 
        cursor.point_to(mention)