import pytest
from songs.model import *


def test_create_song():
	lyrics_text = read_file('songs/tests/led_zeppelin_-_stairway_to_heaven.txt')
	song = Song('Led Zeppelin', 'Stairway to Heaven', lyrics_text)
	assert song.title == SongTitle('Led Zeppelin', 'Stairway to Heaven')
	assert song.lyrics.text == lyrics_text


def test_null_song():
	null_song = NullSong()
	assert null_song.title == SongTitle('', '')
	assert null_song.lyrics.text == ''


def read_file(filename):
    file = open(filename, 'r')
    return file.read()