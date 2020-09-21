import logging

logger = logging.getLogger()


def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    try:
        twitter_api.update_status(str(mixed_lyrics))
    except:
        logger.error('Skipping tweet.', exc_info=True)


def reply_to_mentions(mention_history, composer):
    mentions = mention_history.since_last_persisted()

    for mention in mentions:
        composer.reply(mention)
        mention_history.add(mention)
