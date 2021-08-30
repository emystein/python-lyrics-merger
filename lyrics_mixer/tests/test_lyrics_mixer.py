import pytest
from unittest.mock import Mock

from songs.model import Paragraphs, SongTitle, Lyrics, Song
from songs.tests.fixtures.songs import stairway_to_heaven_title, born_to_be_wild_title, stairway_to_heaven, born_to_be_wild
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, MixedLyrics, \
    MixedSongsTitle
from lyrics_mixer.tests.fixtures.mixer import lyrics_mix

title = SongTitle('Led Zeppelin', 'Stairway to Heaven')
paragraphs = Paragraphs.from_text('line 1\nline 2\n\nline 3\nline 4\n\n')
lyrics = Lyrics(title, paragraphs)
song = Song(title, lyrics)

@pytest.fixture
def lyrics_mixer():
    mock_lyrics_library = Mock()
    return LyricsMixer(mock_lyrics_library, LineInterleaveLyricsMix())


def test_mix_two_random_lyrics(lyrics_mix):
    mock_lyrics_library = Mock()

    mixer = LyricsMixer(mock_lyrics_library, lyrics_mix)

    mock_lyrics_library.get_random_lyrics.return_value = song

    mixed_lyrics = mixer.mix_two_random_lyrics()

    assert mixed_lyrics.has_content()


def test_mix_random_lyrics_by_artists(lyrics_mix):
    mock_lyrics_library = Mock()

    mixer = LyricsMixer(mock_lyrics_library, lyrics_mix)

    mock_lyrics_library.get_random_lyrics_by_artist.return_value = song

    mixed_lyrics = mixer.mix_random_lyrics_by_artists('Led Zeppelin', 'Steppenwolf')

    assert mixed_lyrics.has_content()


def test_mix_specific_lyrics(lyrics_mix, stairway_to_heaven_title, born_to_be_wild_title):
    mock_lyrics_library = Mock()

    mixer = LyricsMixer(mock_lyrics_library, lyrics_mix)

    mock_lyrics_library.get_lyrics.return_value = song

    mixed_lyrics = mixer.mix_specific_lyrics(stairway_to_heaven_title, born_to_be_wild_title)

    assert mixed_lyrics.has_content()


def test_exception_on_mix_lyrics(lyrics_mixer):
    mock_lyrics_picker = Mock()

    mock_lyrics_picker.pick.side_effect = RuntimeError('Download error')

    assert lyrics_mixer.mix_lyrics(mock_lyrics_picker).is_empty()


def test_mixed_lyrics(stairway_to_heaven, born_to_be_wild):
    paragraphs_text = 'paragraph1\n\nparagraph2\n\n'
    paragraphs = Paragraphs.from_text(paragraphs_text)

    mixed_lyrics = MixedLyrics.with_paragraphs([stairway_to_heaven, born_to_be_wild], paragraphs)

    assert mixed_lyrics.title == MixedSongsTitle([stairway_to_heaven, born_to_be_wild])
    assert mixed_lyrics.text == paragraphs_text
