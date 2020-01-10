import pytest
from lyrics_mixer.tests.fixtures.mocks import lyrics_library_mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mixer import LyricsMixer
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix
from lyrics_mixer.mixed_lyrics import MixedLyrics, EmptyMixedLyrics


lyrics_mix_strategy = LineInterleaveLyricsMix()


def test_two_random_songs_mixer(lyrics_library_mock, song1, song2):
	mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

	lyrics_library_mock.get_random_songs.return_value = [song1, song2]

	mixed_lyrics = mixer.mix_two_random_lyrics()

	assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_two_random_songs_by_artists_mixer(lyrics_library_mock, song1, song2):
	mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

	lyrics_library_mock.get_random_songs_by_artists.return_value = [song1, song2]

	mixed_lyrics = mixer.mix_random_lyrics_by_artists(song1.title.artist, song2.title.artist)

	assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_two_specific_songs_mixer(lyrics_library_mock, song1, song2):
	mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

	lyrics_library_mock.get_songs.return_value = [song1, song2]

	mixed_lyrics = mixer.mix_two_specific_lyrics(song1.title, song2.title)

	assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_error_on_lyrics_download(lyrics_library_mock, song1, song2):
	lyrics_library_mock.get_random_songs.side_effect = RuntimeError('Cannot download lyrics')

	mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

	with pytest.raises(Exception):
		mixer.mix_two_random_lyrics()
