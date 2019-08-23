import pytest
from unittest.mock import Mock 
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mixers import *
from lyrics_mixer.mixed_lyrics import *


def test_two_random_songs_mixer(song1, song2):
	lyrics_api_client = Mock()
	lyrics_mix_strategy = Mock()
	lyrics_api_client.get_random_songs.return_value = [song1, song2]
	expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])
	lyrics_mix_strategy.mix.return_value = expected_mixed_lyrics

	mixer = RandomSongPairLyricsMixer(lyrics_api_client, lyrics_mix_strategy)
	mixed_lyrics = mixer.mix_lyrics()

	lyrics_api_client.get_random_songs.assert_called_once_with(2)
	lyrics_mix_strategy.mix.assert_called_once_with(song1, song2)
	assert mixed_lyrics == expected_mixed_lyrics


def test_two_random_songs_by_artists_mixer(song1, song2):
	lyrics_api_client = Mock()
	lyrics_mix_strategy = Mock()
	lyrics_api_client.get_random_songs_by_artists.return_value = [song1, song2]
	expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])
	lyrics_mix_strategy.mix.return_value = expected_mixed_lyrics

	mixer = RandomByArtistsSongPairLyricsMixer(lyrics_api_client, lyrics_mix_strategy, song1.title.artist, song2.title.artist)
	mixed_lyrics = mixer.mix_lyrics()

	lyrics_api_client.get_random_songs_by_artists.assert_called_once_with([song1.title.artist, song2.title.artist])
	lyrics_mix_strategy.mix.assert_called_once_with(song1, song2)
	assert mixed_lyrics == expected_mixed_lyrics


def test_two_specific_songs_mixer(song1, song2):
	lyrics_api_client = Mock()
	lyrics_mix_strategy = Mock()
	lyrics_api_client.get_songs.return_value = [song1, song2]
	expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])
	lyrics_mix_strategy.mix.return_value = expected_mixed_lyrics

	mixer = SpecificSongPairLyricsMixer(lyrics_api_client, lyrics_mix_strategy, song1.title, song2.title)
	mixed_lyrics = mixer.mix_lyrics()

	lyrics_api_client.get_songs.assert_called_once_with([song1.title, song2.title])
	lyrics_mix_strategy.mix.assert_called_once_with(song1, song2)
	assert mixed_lyrics == expected_mixed_lyrics


def test_error_while_picking_songs_creates_an_empty_mixed_lyrics():
	lyrics_api_client = Mock()
	lyrics_mix_strategy = Mock()
	lyrics_api_client.get_random_songs.side_effect = RuntimeError('Song not found')

	mixer = RandomSongPairLyricsMixer(lyrics_api_client, lyrics_mix_strategy)
	mixed_lyrics = mixer.mix_lyrics()

	lyrics_api_client.get_random_songs.assert_called_once()
	assert mixed_lyrics == EmptyMixedLyrics()
