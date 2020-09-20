import logging

logger = logging.getLogger()


def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    try:
        twitter_api.update_status(str(mixed_lyrics))
    except:
        logger.error('Skipping tweet.', exc_info=True)


def reply_to_mentions(twitter_api, composer, reply_cursor):
    mentions = twitter_api.mentions_since(reply_cursor.position)

    for mention in mentions:
        composer.reply(mention)
        reply_cursor.point_to(mention)
