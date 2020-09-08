import logging


logger = logging.getLogger()


def tweet_random_lyrics(twitter_api, lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    twitter_api.update_status(str(mixed_lyrics)) 


def reply_to_mentions(twitter_api, tweet_parser, lyrics_mixer):
    reply_cursor = MentionsReplyCursor()

    logger.info(f"Mentions reply cursor at position: {reply_cursor.position}")

    mentions = twitter_api.mentions_since(reply_cursor.position)

    for mention in mentions:
        reply = TweetReply(mention).parse_with(tweet_parser).compose_reply(lyrics_mixer)
        reply.send()
        reply_cursor.point_to(reply)
