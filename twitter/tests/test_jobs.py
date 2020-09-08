from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMixStrategy
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser
import twitter
import pytest
from unittest.mock import Mock
from twitter.tests.model import FakeTweet
from wikia.lyrics_api_client import WikiaLyricsApiClient


def test_reply_to_mentions():
    song_titles_parser = SongTitlesParser(SongTitlesSplitter())
    lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMixStrategy())

    twitter_api = Mock()

    mentions = [FakeTweet(1, 'emenendez', '@lyricsmixer mix U2 and A-ha')]

    twitter_api.mentions_since.return_value = mentions

    lyrics_mixer = Mock()

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = 'Blah'

    lyrics_mixer.twitter.jobs.reply_to_mentions(twitter_api, song_titles_parser, lyrics_mixer)
