import logging
from twitter_bot.persistence import MentionsReplyCursor
from twitter_bot.twitter import Composer


logger = logging.getLogger()


def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    try:
        twitter_api.update_status(str(mixed_lyrics))
    except:
        logger.error('Skipping tweet.', exc_info=True)


def reply_to_mentions(twitter_api, tweet_parser, lyrics_mixer):
    reply_cursor = MentionsReplyCursor()

    logger.info(f"Mentions reply cursor at position: {reply_cursor.position}")

    mentions = twitter_api.mentions_since(reply_cursor.position)

    for mention in mentions:
        logger.info(f"Replying to mention: {mention}")
        reply = Composer(tweet_parser, lyrics_mixer).compose_reply(mention)
        reply.send()
        reply_cursor.point_to(reply)
