import logging
import time
import twitter
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, EmptyMixedLyrics
from wikia.lyrics_api_client import WikiaLyricsApiClient
from lyrics_mixer.artists_parser import ArtistsParser
from lyrics_mixer.orm import StreamCursor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())

def tweet_random_lyrics(twitter_api):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    twitter_api.update_status(mixed_lyrics) 


def reply_to_mentions(twitter_api):
    cursor, created = StreamCursor.get_or_create(key = 'twitter')
    cursor.position = check_mentions(twitter_api, cursor.position, MixLyricsReplyStrategy(ArtistsParser(), lyrics_mixer))
    cursor.save()


class MixLyricsReplyStrategy(object):
    def __init__(self, input_parser, lyrics_mixer):
        self.input_parser = input_parser
        self.lyrics_mixer = lyrics_mixer
    
    def get_reply_for(self, tweet):
        logger.info(f"Mixing lyrics requested by: {tweet.user.name}, using input: '{tweet.text}'")
        parsed = self.input_parser.parse(tweet.text)
        mixed_lyrics = self.lyrics_mixer.mix_random_lyrics_by_artists(parsed.artist1, parsed.artist2)
        return f"@{tweet.user.name} {mixed_lyrics}"


def check_mentions(twitter_api, since_id, reply_strategy):
    logger.info(f"Checking mentions since: {since_id}")

    new_since_id = since_id
    mentions = twitter_api.mentions_since(since_id)
    for tweet in mentions:
        reply_text = reply_strategy.get_reply_for(tweet)
        twitter_api.reply_tweet_with(tweet, reply_text)
        new_since_id = tweet.id
    return new_since_id

