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


def reply_to_mentions(twitter_api, tweet_parser, lyrics_mixer, reply_cursor):
    composer = Composer(tweet_parser, lyrics_mixer)

    mentions = twitter_api.mentions_since(reply_cursor.position)

    for mention in mentions:
        composer.reply(mention)
        reply_cursor.point_to(mention)
