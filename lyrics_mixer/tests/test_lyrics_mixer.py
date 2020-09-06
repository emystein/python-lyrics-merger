import pytest
from unittest.mock import Mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMixStrategy, MixedLyrics


lyrics_mix = LineInterleaveLyricsMixStrategy()


def test_exception_on_mix_lyrics():
    lyrics_library_mock = Mock()

    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix)

    lyrics_picker_mock = Mock()

    lyrics_picker_mock.pick_two.side_effect = RuntimeError('Download error')

    assert mixer.mix_lyrics(lyrics_picker_mock) == MixedLyrics.empty()


def test_mixed_lyrics(song1, song2):
    expected = lyrics_mix.mix(song1, song2)

    mixed_lyrics = MixedLyrics(song1, song2, [], expected.paragraphs)

    assert mixed_lyrics.title == str(song1.title) + ', ' + str(song2.title)
    assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)
