import pytest
from lyrics_mixer.tests.fixtures.mocks import lyrics_library_mock, lyrics_mix_strategy_mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.dispatcher import Dispatcher
from lyrics_mixer.mixed_lyrics import MixedLyrics, EmptyMixedLyrics

def test_two_random_songs_mixer(lyrics_library_mock, lyrics_mix_strategy_mock, song1, song2):
	mixer = Dispatcher(lyrics_library_mock, lyrics_mix_strategy_mock)

	lyrics_library_mock.get_random_songs.return_value = [song1, song2]
	expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])
	lyrics_mix_strategy_mock.mix.return_value = expected_mixed_lyrics

	mixed_lyrics = mixer.mix_two_random_lyrics()

	lyrics_library_mock.get_random_songs.assert_called_once_with(2)
	lyrics_mix_strategy_mock.mix.assert_called_once_with(song1, song2)
	assert mixed_lyrics == expected_mixed_lyrics


def test_two_random_songs_by_artists_mixer(lyrics_library_mock, lyrics_mix_strategy_mock, song1, song2):
	mixer = Dispatcher(lyrics_library_mock, lyrics_mix_strategy_mock)

	lyrics_library_mock.get_random_songs_by_artists.return_value = [song1, song2]
	expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])
	lyrics_mix_strategy_mock.mix.return_value = expected_mixed_lyrics

	mixed_lyrics = mixer.mix_random_lyrics_by_artists(song1.title.artist, song2.title.artist)

	lyrics_library_mock.get_random_songs_by_artists.assert_called_once_with([song1.title.artist, song2.title.artist])
	lyrics_mix_strategy_mock.mix.assert_called_once_with(song1, song2)
	assert mixed_lyrics == expected_mixed_lyrics


def test_two_specific_songs_mixer(lyrics_library_mock, lyrics_mix_strategy_mock, song1, song2):
	mixer = Dispatcher(lyrics_library_mock, lyrics_mix_strategy_mock)

	lyrics_library_mock.get_songs.return_value = [song1, song2]
	expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])
	lyrics_mix_strategy_mock.mix.return_value = expected_mixed_lyrics

	mixed_lyrics = mixer.mix_two_specific_lyrics(song1.title, song2.title)

	lyrics_library_mock.get_songs.assert_called_once_with([song1.title, song2.title])
	lyrics_mix_strategy_mock.mix.assert_called_once_with(song1, song2)
	assert mixed_lyrics == expected_mixed_lyrics


def test_error_on_lyrics_download(lyrics_library_mock, lyrics_mix_strategy_mock, song1, song2):
	lyrics_library_mock.get_random_songs.side_effect = RuntimeError('Cannot download lyrics')

	mixer = Dispatcher(lyrics_library_mock, lyrics_mix_strategy_mock)

	mixed_lyrics = mixer.mix_two_random_lyrics()

	assert mixed_lyrics == EmptyMixedLyrics()
