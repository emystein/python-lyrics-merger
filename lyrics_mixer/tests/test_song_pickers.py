import pytest
from unittest.mock import Mock 
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.song_pickers import *


def test_two_random_songs_picker(song1, song2):
	lyrics_api_client = Mock()
	lyrics_api_client.get_random_songs.return_value = [song1, song2]

	picker = TwoRandomSongsPicker(lyrics_api_client)
	song_pair = picker.pick_song_pair()

	lyrics_api_client.get_random_songs.assert_called_once_with(2)
	assert song_pair.song1 == song1
	assert song_pair.song2 == song2


def test_two_random_songs_by_artists_picker(song1, song2):
	lyrics_api_client = Mock()
	lyrics_api_client.get_random_songs_by_artists.return_value = [song1, song2]

	picker = TwoRandomSongsByArtistsPicker(lyrics_api_client, song1.title.artist, song2.title.artist)
	song_pair = picker.pick_song_pair()

	lyrics_api_client.get_random_songs_by_artists.assert_called_once_with([song1.title.artist, song2.title.artist])
	assert song_pair.song1 == song1
	assert song_pair.song2 == song2


def test_two_specific_songs_picker(song1, song2):
	lyrics_api_client = Mock()
	lyrics_api_client.get_songs.return_value = [song1, song2]

	picker = TwoSpecificSongsPicker(lyrics_api_client, song1.title, song2.title)
	song_pair = picker.pick_song_pair()

	lyrics_api_client.get_songs.assert_called_once_with([song1.title, song2.title])
	assert song_pair.song1 == song1
	assert song_pair.song2 == song2


def test_error_while_picking_songs_creates_an_empty_song_pair():
	lyrics_api_client = Mock()
	lyrics_api_client.get_random_songs.side_effect = RuntimeError('Song not found')

	picker = TwoRandomSongsPicker(lyrics_api_client)
	song_pair = picker.pick_song_pair()

	lyrics_api_client.get_random_songs.assert_called_once()
	assert song_pair == EmptySongPair()
