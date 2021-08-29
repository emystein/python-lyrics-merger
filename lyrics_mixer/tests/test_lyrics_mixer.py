import pytest
from unittest.mock import Mock

from songs.model import Paragraphs
from songs.tests.fixtures.songs import stairway_to_heaven, born_to_be_wild
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, MixedLyrics, \
    MixedSongsTitle


@pytest.fixture
def lyrics_mixer():
    mock_lyrics_library = Mock()
    return LyricsMixer(mock_lyrics_library, LineInterleaveLyricsMix())


def test_exception_on_mix_lyrics(lyrics_mixer):
    mock_lyrics_picker = Mock()

    mock_lyrics_picker.pick.side_effect = RuntimeError('Download error')

    assert lyrics_mixer.mix_lyrics(mock_lyrics_picker) == MixedLyrics.empty()


def test_mixed_lyrics(stairway_to_heaven, born_to_be_wild):
    paragraphs_text = 'paragraph1\n\nparagraph2\n\n'
    paragraphs = Paragraphs.from_text(paragraphs_text)

    mixed_lyrics = MixedLyrics.with_paragraphs([stairway_to_heaven, born_to_be_wild], paragraphs)

    assert mixed_lyrics.title == MixedSongsTitle([stairway_to_heaven, born_to_be_wild])
    assert mixed_lyrics.text == paragraphs_text
