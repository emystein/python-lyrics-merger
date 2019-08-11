import tweepy
import logging
import time
import twitter
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, EmptyMixedLyrics
from wikia.lyrics_api_client import WikiaLyricsApiClient
from lyrics_mixer.artists_parser import ArtistsParser
from lyrics_mixer.orm import StreamCursor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def tweet_random_lyrics(twitter_api):
    logger.info("About to mix lyrics")
    lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    tweet = str(mixed_lyrics)[:twitter.MAX_TWEET_LENGTH]
    twitter_api.update_status(tweet) 


def reply_to_mentions(twitter_api):
    cursor, created = StreamCursor.get_or_create(key = 'twitter')
    reply_strategy = MixLyricsReplyStrategy()
    cursor.position = check_mentions(twitter_api, cursor.position, reply_strategy)
    cursor.save()


class MixLyricsReplyStrategy(object):
    def __init__(self):
        self.input_parser = ArtistsParser()
        self.mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())
    
    def get_reply_for(self, tweet):
        logger.info(f"Mixing lyrics requested by: {tweet.user.name}, using input: '{tweet.text}'")
        mixed_lyrics = str(self.mix_lyrics_parsing_input(tweet.text))
        return f"@{tweet.user.name} {mixed_lyrics}"

    def mix_lyrics_parsing_input(self, text):
        try:
            parsed = self.input_parser.parse(text)
            mixed_lyrics = self.mixer.mix_random_lyrics_by_artists(parsed.artist1, parsed.artist2)
        except Exception as e:
            logger.error("Error mixing lyrics, returning empty lyrics", exc_info=True)
            mixed_lyrics = EmptyMixedLyrics()
        logger.info(f"Mixed lyrics: {mixed_lyrics.title}")
        return mixed_lyrics


def check_mentions(api, since_id, reply_strategy):
    logger.info(f"Checking mentions since: {since_id}")

    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        reply_text = reply_strategy.get_reply_for(tweet)
        reply_tweet_with(api, tweet, reply_text)
    return new_since_id


# TODO make a function of api (monkey-patch api?)
def reply_tweet_with(api, tweet, reply_text):
    api.update_status(status = reply_text[:twitter.MAX_TWEET_LENGTH], in_reply_to_status_id = tweet.id)
