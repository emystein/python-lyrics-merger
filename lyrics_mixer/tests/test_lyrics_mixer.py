import pytest
from unittest.mock import Mock

from songs.model import Paragraphs
from songs.tests.fixtures.songs import stairway_to_heaven, born_to_be_wild
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, MixedLyrics


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
    paragraphs = Paragraphs(paragraphs_text)

    mixed_lyrics = MixedLyrics([stairway_to_heaven.title, born_to_be_wild.title], paragraphs)

    assert mixed_lyrics.title == f"{stairway_to_heaven.title}, {born_to_be_wild.title}"
    assert mixed_lyrics.text == paragraphs_text
