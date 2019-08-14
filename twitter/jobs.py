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
    cursor = MentionsReplyCursor.get_or_create()
    logger.info(f"Replying to mentions since: {cursor.position}")
    mentions = twitter_api.mentions_since(cursor.position)
    reply_strategy = MixLyricsReplyStrategy(ArtistsParser(), lyrics_mixer)

    for mention in mentions:
        mention.reply_with(reply_strategy) 

    cursor.update_from_mentions(mentions)


class MixLyricsReplyStrategy(object):
    def __init__(self, input_parser, lyrics_mixer):
        self.input_parser = input_parser
        self.lyrics_mixer = lyrics_mixer
    
    def get_reply_for(self, tweet):
        logger.info(f"Mixing lyrics requested by: {tweet.user.name}, using input: '{tweet.text}'")
        parsed = self.input_parser.parse(tweet.text)
        mixed_lyrics = self.lyrics_mixer.mix_random_lyrics_by_artists(parsed.artist1, parsed.artist2)
        return f"@{tweet.user.name} {mixed_lyrics}"


class MentionsReplyCursor(object):
    def __init__(self, wrapped_cursor):
        self.wrapped_cursor = wrapped_cursor

    def get_or_create():
        cursor, created = StreamCursor.get_or_create(key = 'twitter') 
        return MentionsReplyCursor(cursor) 

    def position(self):
        return self.wrapped_cursor.position

    def update_from_mentions(self, mentions):
        new_since_id = mentions[-1].id if len(mentions) > 0 else 1
        self.wrapped_cursor.position = max(self.wrapped_cursor.position, new_since_id)
        self.wrapped_cursor.save()
