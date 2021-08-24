import pytest
from unittest.mock import Mock

from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, MixedLyrics


@pytest.fixture
def lyrics_mixer():
    mock_lyrics_library = Mock()
    return LyricsMixer(mock_lyrics_library, LineInterleaveLyricsMix())


def test_exception_on_mix_lyrics(lyrics_mixer):
    mock_lyrics_picker = Mock()

    mock_lyrics_picker.pick.side_effect = RuntimeError('Download error')

    assert lyrics_mixer.mix_lyrics(mock_lyrics_picker) == MixedLyrics.empty()


def test_mixed_lyrics(song1, song2):
    lines = 'line1\nline2'
    paragraphs = ['line1', 'line2']

    mixed_lyrics = MixedLyrics([song1, song2], lines, paragraphs)

    assert mixed_lyrics.title == f"{song1.title}, {song2.title}"
    assert mixed_lyrics.text == '\n\n'.join(paragraphs)
