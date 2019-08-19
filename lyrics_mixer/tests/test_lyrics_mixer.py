import pytest
from unittest.mock import Mock 
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mixer import LyricsMixer, MixedLyrics


def test_two_random_songs_mixer(song1, song2):
	lyrics_api_client = Mock()
	lyrics_mix_strategy = Mock()
	
	mixer = LyricsMixer(lyrics_api_client, lyrics_mix_strategy)

	lyrics_api_client.get_random_songs.return_value = [song1, song2]
	expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])
	lyrics_mix_strategy.mix_lyrics.return_value = expected_mixed_lyrics

	mixed_lyrics = mixer.mix_two_random_lyrics()

	lyrics_api_client.get_random_songs.assert_called_once_with(2)
	lyrics_mix_strategy.mix_lyrics.assert_called_once_with(song1, song2)
	assert mixed_lyrics == expected_mixed_lyrics


def test_two_random_songs_by_artists_mixer(song1, song2):
	lyrics_api_client = Mock()
	lyrics_mix_strategy = Mock()
	
	mixer = LyricsMixer(lyrics_api_client, lyrics_mix_strategy)

	lyrics_api_client.get_random_songs_by_artists.return_value = [song1, song2]
	expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])
	lyrics_mix_strategy.mix_lyrics.return_value = expected_mixed_lyrics

	mixed_lyrics = mixer.mix_random_lyrics_by_artists(song1.title.artist, song2.title.artist)

	lyrics_api_client.get_random_songs_by_artists.assert_called_once_with([song1.title.artist, song2.title.artist])
	lyrics_mix_strategy.mix_lyrics.assert_called_once_with(song1, song2)
	assert mixed_lyrics == expected_mixed_lyrics


def test_two_specific_songs_mixer(song1, song2):
	lyrics_api_client = Mock()
	lyrics_mix_strategy = Mock()
	
	mixer = LyricsMixer(lyrics_api_client, lyrics_mix_strategy)

	lyrics_api_client.get_songs.return_value = [song1, song2]
	expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])
	lyrics_mix_strategy.mix_lyrics.return_value = expected_mixed_lyrics

	mixed_lyrics = mixer.mix_two_specific_lyrics(song1.title, song2.title)

	lyrics_api_client.get_songs.assert_called_once_with([song1.title, song2.title])
	lyrics_mix_strategy.mix_lyrics.assert_called_once_with(song1, song2)
	assert mixed_lyrics == expected_mixed_lyrics