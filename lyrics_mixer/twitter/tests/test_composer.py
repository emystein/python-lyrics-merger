import pytest
from unittest.mock import Mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.twitter.composer import MixLyricsComposer
from lyrics_mixer.song_titles_parser import ParsedArtists
from lyrics_mixer.lyrics_mixer import MixedLyrics
from twitter.tests.model import TweetForTest


lyrics_mixer=Mock()

composer = MixLyricsComposer(lyrics_mixer)

parsed = ParsedArtists(['Led Zeppelin', 'Steppenwolf'])


def test_reply(song1, song2):
    tweet = TweetForTest('emenendez', 'text')

    expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])

    lyrics_mixer.mix_parsed_song_titles.return_value = expected_mixed_lyrics

    result = composer.write_reply(tweet, parsed)

    assert result == f"@{tweet.user.name} {expected_mixed_lyrics}"
