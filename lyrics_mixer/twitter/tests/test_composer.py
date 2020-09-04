import pytest
from unittest.mock import Mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.twitter.composer import MixLyricsComposer
from lyrics_mixer.song_titles_parser import ParsedArtists
from lyrics_mixer.lyrics_mixer import MixedLyrics
from twitter.tests.model import Tweet


def test_reply(song1, song2):
    lyrics_mixer = Mock()

    expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])

    lyrics_mixer.mix_parsed_song_titles.return_value = expected_mixed_lyrics

    composer = MixLyricsComposer(lyrics_mixer)

    result = composer.write_reply(Tweet('emenendez', 'text'),
                                  ParsedArtists(['Led Zeppelin', 'Steppenwolf']))

    assert result == f"@emenendez {expected_mixed_lyrics}"
