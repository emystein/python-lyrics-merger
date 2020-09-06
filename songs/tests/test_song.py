import pytest
from songs.model import *


def test_create_song():
	lyrics_text = read_file('songs/tests/led_zeppelin_-_stairway_to_heaven.txt')
	song = Song('Led Zeppelin', 'Stairway to Heaven', lyrics_text)
	assert song.artist == 'Led Zeppelin'
	assert song.title == SongTitle('Led Zeppelin', 'Stairway to Heaven')
	assert song.lyrics == Lyrics(lyrics_text)


def test_none_song():
	none_song = Song.none()
	assert none_song.artist == ''
	assert none_song.title == SongTitle.empty()
	assert none_song.lyrics == Lyrics.empty()


def read_file(filename):
    file = open(filename, 'r')
    return file.read()