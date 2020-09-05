import pytest
from songs.model import *


def test_create_song():
	lyrics_text = read_file('songs/tests/led_zeppelin_-_stairway_to_heaven.txt')
	song = Song('Led Zeppelin', 'Stairway to Heaven', lyrics_text)
	assert song.artist == 'Led Zeppelin'
	assert song.title == 'Stairway to Heaven'
	assert song.lyrics == Lyrics(lyrics_text)


def test_null_song():
	null_song = NoneSong()
	assert null_song.artist == ''
	assert null_song.title == ''
	assert null_song.lyrics == EmptyLyrics()


def read_file(filename):
    file = open(filename, 'r')
    return file.read()