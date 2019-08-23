import pytest
from unittest.mock import Mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.song_lyrics_mixers import SongPair, EmptySongPair
from lyrics_mixer.mixed_lyrics import MixedLyrics, EmptyMixedLyrics


def test_song_pair_mix_lyrics(song1, song2):
	lyrics_mix_strategy = Mock()
	lyrics_mix_strategy.mix.return_value = MixedLyrics(song1, song2, [], [])

	song_pair = SongPair(song1, song2)
	song_pair.mix_lyrics(lyrics_mix_strategy)

	lyrics_mix_strategy.mix.assert_called_once_with(song1, song2)


def test_song_pair_equals(song1, song2):
	song_pair1 = SongPair(song1, song2)
	song_pair2 = SongPair(song1, song2)

	assert song_pair1 == song_pair2


def test_empty_song_pair_mix_lyrics():
	lyrics_mix_strategy = Mock()

	song_pair = EmptySongPair()

	assert song_pair.mix_lyrics(lyrics_mix_strategy) == EmptyMixedLyrics()


def test_empty_song_pair_equals():
	song_pair1 = EmptySongPair()
	song_pair2 = EmptySongPair()

	assert song_pair1 == song_pair2