import time
import twitter
from twitter.persistence import MentionsReplyCursor

def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    twitter_api.update_status(mixed_lyrics) 


def reply_to_mentions(twitter_api, mention_parser, reply_strategy):
    # TODO: pass MentionsReplyCursor as parameter?
    cursor = MentionsReplyCursor()
    mentions = twitter_api.mentions_since(cursor.position)
    for mention in mentions:
        mention.reply_using(mention_parser, reply_strategy) 
        cursor.point_to(mention)