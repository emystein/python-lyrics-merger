from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMixStrategy
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser
import lyrics_mixer.twitter.jobs
import pytest
from unittest.mock import Mock
from wikia.lyrics_api_client import WikiaLyricsApiClient


def test_reply_to_mentions():
    song_titles_parser = SongTitlesParser(SongTitlesSplitter())
    lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMixStrategy())

    twitter_api = Mock()
    lyrics_mixer = Mock()

    mentions = [FakeTweet(1, 'emenendez', '@lyricsmixer mix U2 and A-ha')]

    twitter_api.mentions_since.return_value = mentions

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = 'Blah'

    lyrics_mixer.twitter.jobs.reply_to_mentions(twitter_api, song_titles_parser, lyrics_mixer)


# TODO: unify with twitter.tests.model classes
class User:
    def __init__(self, name):
        self.name = name


class FakeTweet:
    def __init__(self, id, username, text):
        self.id = id
        self.author = User(username)
        self.text = text
