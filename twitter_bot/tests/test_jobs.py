from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMixStrategy
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser, ParsedArtists
from peewee import *
import pytest
from unittest.mock import Mock
from twitter.tests.model import FakeTweet
from twitter.persistence import StreamCursor
from twitter.twitter import Tweet
import twitter_bot.jobs
from lyrics_mixer.lyrics_data_source import LyricsDataSource

database = SqliteDatabase(':memory:')
database.bind([StreamCursor])
database.create_tables([StreamCursor])

song_titles_parser = SongTitlesParser(SongTitlesSplitter())

lyrics_mixer = LyricsMixer(
    LyricsDataSource(), LineInterleaveLyricsMixStrategy())


@pytest.mark.slow_integration_test
def test_random_lyrics():
    twitter_api = Mock()

    twitter_bot.jobs.tweet_random_lyrics(twitter_api, lyrics_mixer)


@pytest.mark.slow_integration_test
def test_reply_to_mentions():
    twitter_api = Mock()

    mentions = [Tweet(twitter_api, FakeTweet(
        1, 'emystein', '@lyricsmixer mix U2 and INXS'))]

    twitter_api.mentions_since.return_value = mentions

    twitter_bot.jobs.reply_to_mentions(
        twitter_api, song_titles_parser, lyrics_mixer)
