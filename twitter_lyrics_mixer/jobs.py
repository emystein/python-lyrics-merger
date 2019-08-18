import time
from twitter.persistence import MentionsReplyCursor
from twitter.twitter import TweetReply

def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    twitter_api.update_status(mixed_lyrics) 


def reply_to_mentions(twitter_api, mention_parser, reply_strategy):
    reply_cursor = MentionsReplyCursor()
    mentions = twitter_api.mentions_since(reply_cursor.position)
    # TODO model TweetReply(mention).parse_with(mention_parser) as LyricsMixParsedTweet
    replies = map(lambda mention: TweetReply(mention).parse_with(mention_parser).write_with(reply_strategy), mentions)
    send(replies)


def send(replies):
    reply_cursor = MentionsReplyCursor()
    for reply in replies:
        reply.send()
        reply_cursor.point_to(reply)