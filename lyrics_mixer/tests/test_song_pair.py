import pytest
from unittest.mock import Mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.song_pair import SongPair, EmptySongPair
from lyrics_mixer.mixed_lyrics import MixedLyrics, EmptyMixedLyrics
from songs.model import NullSong

def test_song_pair_created_with_picked_songs(song1, song2):
	song_picker = Mock()

	song_picker.pick_song_pair.return_value = [song1, song2]

	song_pair = SongPair.picked_using(song_picker)

	song_picker.pick_song_pair.assert_called_once()
	assert song_pair.song1 == song1
	assert song_pair.song2 == song2


def test_song_pair_mix_lyrics(song1, song2):
	song_picker = Mock()
	lyrics_mix_strategy = Mock()

	song_picker.pick_song_pair.return_value = [song1, song2]
	lyrics_mix_strategy.mix.return_value = MixedLyrics(song1, song2, [], [])

	song_pair = SongPair.picked_using(song_picker)
	song_pair.mix_lyrics(lyrics_mix_strategy)

	song_picker.pick_song_pair.assert_called_once()
	lyrics_mix_strategy.mix.assert_called_once_with(song1, song2)


def test_error_while_picking_songs_creates_an_empty_song_pair():
	song_picker = Mock()

	song_picker.pick_song_pair.side_effect = RuntimeError('Song not found')

	song_pair = SongPair.picked_using(song_picker)

	song_picker.pick_song_pair.assert_called_once()
	assert song_pair == EmptySongPair()

def test_empty_song_pair_creation():
	song_pair = EmptySongPair()

	assert song_pair.song1 == NullSong()
	assert song_pair.song2 == NullSong()


def test_empty_song_pair_mix_lyrics():
	lyrics_mix_strategy = Mock()

	song_pair = EmptySongPair()

	assert song_pair.mix_lyrics(lyrics_mix_strategy) == EmptyMixedLyrics()