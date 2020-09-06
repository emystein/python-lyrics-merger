import pytest
from unittest.mock import Mock
from lyrics_mixer.tests.fixtures.mocks import lyrics_library_mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.song_titles_parser import ParsedArtists
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMixStrategy, ParagraphInterleaveLyricsMixStrategy, MixedLyrics


lyrics_mix_strategy = LineInterleaveLyricsMixStrategy()


def test_exception_on_mix_lyrics(lyrics_library_mock):
    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

    lyrics_picker = Mock()

    lyrics_picker.pick_two.side_effect = RuntimeError('Download error')

    assert mixer.mix_lyrics(lyrics_picker) == MixedLyrics.empty()


def test_mixed_lyrics(song1, song2):
    lyrics_editor = ParagraphInterleaveLyricsMixStrategy()

    expected = lyrics_editor.mix(song1, song2)

    mixed_lyrics = MixedLyrics(song1, song2, [], expected.paragraphs)

    assert mixed_lyrics.title == str(song1.title) + ', ' + str(song2.title)
    assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)
