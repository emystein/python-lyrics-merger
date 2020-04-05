import logging
from twitter.persistence import MentionsReplyCursor


logger = logging.getLogger()


def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    twitter_api.update_status(str(mixed_lyrics)) 


def reply_to_mentions(twitter_api, tweet_reply_factory):
    reply_cursor = MentionsReplyCursor()
    logger.info(f"Mentions reply cursor at position: {reply_cursor.position}")
    mentions = twitter_api.mentions_since(reply_cursor.position)
    replies = tweet_reply_factory.create_from_many(mentions)
    send(replies)


def send(replies):
    reply_cursor = MentionsReplyCursor()

    for reply in replies:
        reply.send()
        reply_cursor.point_to(reply)