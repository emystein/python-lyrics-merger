import time
from twitter.persistence import MentionsReplyCursor
from twitter.twitter import TweetReply


def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    twitter_api.update_status(mixed_lyrics)


def reply_to_mentions(twitter_api, mention_parser, reply_strategy):
    # TODO: pass MentionsReplyCursor as parameter?
    cursor = MentionsReplyCursor()
    mentions = twitter_api.mentions_since(cursor.position)
    for mention in mentions:
        # mention.reply_using(mention_parser, reply_strategy)
        reply = TweetReply.for_tweet(mention).parse_tweet_with(mention_parser).write_with(reply_strategy)
        reply.send()
        cursor.point_to(mention)
