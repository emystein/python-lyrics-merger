import pytest
from lyrics_mixer.tests.fixtures.mocks import lyrics_library_mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix
from lyrics_mixer.lyrics_mixers import *
from lyrics_mixer.mixed_lyrics import *

lyrics_mix_strategy = LineInterleaveLyricsMix()

def test_two_random_songs_mixer(lyrics_library_mock, song1, song2):
	lyrics_library_mock.get_random_songs.return_value = [song1, song2]

	mixer = RandomLyricsMixer(lyrics_library_mock)
	mixed_lyrics = mixer.mix_lyrics(lyrics_mix_strategy)

	assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_two_random_songs_by_artists_mixer(lyrics_library_mock, song1, song2):
	lyrics_library_mock.get_random_songs_by_artists.return_value = [song1, song2]

	mixer = RandomByArtistsLyricsMixer(lyrics_library_mock, song1.title.artist, song2.title.artist)
	mixed_lyrics = mixer.mix_lyrics(lyrics_mix_strategy)

	assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_two_specific_songs_mixer(lyrics_library_mock, song1, song2):
	lyrics_library_mock.get_songs.return_value = [song1, song2]

	mixer = SpecificLyricsMixer(lyrics_library_mock, song1.title, song2.title)
	mixed_lyrics = mixer.mix_lyrics(lyrics_mix_strategy)

	assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_error_while_picking_songs_creates_an_empty_mixed_lyrics(lyrics_library_mock):
	lyrics_library_mock.get_random_songs.side_effect = RuntimeError('Song not found')

	mixer = RandomLyricsMixer(lyrics_library_mock)
	mixed_lyrics = mixer.mix_lyrics(lyrics_mix_strategy)

	assert mixed_lyrics == EmptyMixedLyrics()
