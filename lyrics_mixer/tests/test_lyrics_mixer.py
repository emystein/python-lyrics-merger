import pytest
from unittest.mock import Mock

from songs.model import SongTitle
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mixer import MixedLyrics
from lyrics_mixer.tests.fixtures.mixer import lyrics_mixer, mock_lyrics_library, lyrics_mix, mixed_lyrics


def test_mix_two_random_lyrics(lyrics_mixer, mock_lyrics_library, mixed_lyrics):
    mock_lyrics_library.get_random_lyrics.side_effect = mixed_lyrics.songs

    assert lyrics_mixer.mix_two_random_lyrics() == mixed_lyrics


def test_mix_random_lyrics_by_artists(lyrics_mixer, mock_lyrics_library, mixed_lyrics):
    mock_lyrics_library.get_random_lyrics_by_artist.side_effect = mixed_lyrics.songs

    assert lyrics_mixer.mix_random_lyrics_by_artists(
        mixed_lyrics.artist1, mixed_lyrics.artist2) == mixed_lyrics


def test_mix_two_specific_lyrics(lyrics_mixer, mock_lyrics_library, mixed_lyrics):
    mock_lyrics_library.get_lyrics.side_effect = mixed_lyrics.songs

    song1, song2 = mixed_lyrics.songs

    assert lyrics_mixer.mix_two_specific_lyrics(
        SongTitle(song1.artist, song1.title), 
        SongTitle(song2.artist, song2.title)) == mixed_lyrics


def test_exception_on_mix_lyrics(lyrics_mixer):
    mock_lyrics_picker = Mock()

    mock_lyrics_picker.pick.side_effect = RuntimeError('Download error')

    assert lyrics_mixer.mix_lyrics(mock_lyrics_picker) == MixedLyrics.empty()


def test_mixed_lyrics(lyrics_mix, song1, song2):
    expected = lyrics_mix.mix(song1, song2)

    mixed_lyrics = MixedLyrics(song1, song2, [], expected.paragraphs)

    assert mixed_lyrics.title == f"{song1.artist} - {song1.title}, {song2.artist} - {song2.title}"
    assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)
