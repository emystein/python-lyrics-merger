import pytest
from lyrics_mixer.tests.fixtures.mocks import lyrics_library_mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mixer import LineInterleaveLyricsMixStrategy, MixedLyrics, EmptyMixedLyrics
from lyrics_mixer.lyrics_pickers import *

lyrics_mix_strategy = LineInterleaveLyricsMixStrategy()


def test_two_random_songs_picker(lyrics_library_mock, song1, song2):
    lyrics_library_mock.get_random_songs.return_value = [song1, song2]

    picker = RandomLyricsPicker(lyrics_library_mock)

    assert picker.pick_two() == [song1, song2]


def test_two_random_songs_by_artists_picker(lyrics_library_mock, song1, song2):
    lyrics_library_mock.get_random_songs_by_artists.return_value = [
        song1, song2]

    picker = RandomByArtistsLyricsPicker(
        lyrics_library_mock, song1.title.artist, song2.title.artist)

    assert picker.pick_two() == [song1, song2]


def test_two_specific_songs_picker(lyrics_library_mock, song1, song2):
    lyrics_library_mock.get_songs.return_value = [song1, song2]

    picker = SpecificLyricsPicker(lyrics_library_mock, song1.title, song2.title)

    assert picker.pick_two() == [song1, song2]


def test_error_while_picking_songs(lyrics_library_mock):
    lyrics_library_mock.get_random_songs.side_effect = RuntimeError(
        'Song not found')

    picker = RandomLyricsPicker(lyrics_library_mock)

    with pytest.raises(Exception):
        picker.pick_two()
