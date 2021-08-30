from unittest.mock import Mock

from songs.model import Paragraphs, SongTitle, Lyrics
from songs.tests import song_factory
from songs.tests.fixtures.songs import stairway_to_heaven_title, born_to_be_wild_title
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix

lyrics = song_factory.stairway_to_heaven_lyrics()
born_to_be_wild_lyrics = song_factory.born_to_be_wild_lyrics()

def test_mix_two_random_lyrics():
    mock_lyrics_library = Mock()

    mixer = LyricsMixer(mock_lyrics_library, LineInterleaveLyricsMix())

    mock_lyrics_library.get_random_lyrics.return_value = lyrics
    mock_lyrics_library.get_random_lyrics.return_value = born_to_be_wild_lyrics

    mixed_lyrics = mixer.mix_two_random_lyrics()

    assert mixed_lyrics.has_content()


def test_mix_random_lyrics_by_artists():
    mock_lyrics_library = Mock()

    mixer = LyricsMixer(mock_lyrics_library, LineInterleaveLyricsMix())

    mock_lyrics_library.get_random_lyrics_by_artist.return_value = lyrics
    mock_lyrics_library.get_random_lyrics_by_artist.return_value = born_to_be_wild_lyrics

    mixed_lyrics = mixer.mix_random_lyrics_by_artists('Led Zeppelin', 'Steppenwolf')

    assert mixed_lyrics.has_content()


def test_mix_specific_lyrics(stairway_to_heaven_title, born_to_be_wild_title):
    mock_lyrics_library = Mock()

    mixer = LyricsMixer(mock_lyrics_library, LineInterleaveLyricsMix())

    mock_lyrics_library.get_lyrics.return_value = lyrics
    mock_lyrics_library.get_lyrics.return_value = born_to_be_wild_lyrics

    mixed_lyrics = mixer.mix_specific_lyrics(stairway_to_heaven_title, born_to_be_wild_title)

    assert mixed_lyrics.has_content()


def test_exception_on_mix_lyrics():
    mock_lyrics_library = Mock()
    mock_lyrics_picker = Mock()

    mixer = LyricsMixer(mock_lyrics_library, mock_lyrics_picker)

    mock_lyrics_picker.pick.side_effect = RuntimeError('Download error')

    assert mixer.mix_lyrics(mock_lyrics_picker).is_empty()

