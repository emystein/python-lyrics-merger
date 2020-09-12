import pytest
from songs.model import Song, SongTitle, Lyrics


def test_create_song():
	lyrics_text = read_file('songs/tests/led_zeppelin_-_stairway_to_heaven.txt')
	title = SongTitle('Led Zeppelin', 'Stairway to Heaven')
	lyrics = Lyrics(lyrics_text)
	song = Song('Led Zeppelin', title, lyrics)
	assert song.artist == 'Led Zeppelin'
	assert song.title == title
	assert song.lyrics == lyrics


def test_song_equals_by_artist_and_title():
	title = SongTitle('Led Zeppelin', 'Stairway to Heaven')
	song1 = Song('Led Zeppelin', title, Lyrics('some lyrics'))
	song2 = Song('Led Zeppelin', title, Lyrics('other lyrics'))
	assert song1 == song2


def test_none_song():
	none_song = Song.none()
	assert none_song.artist == ''
	assert none_song.title == SongTitle.empty()
	assert none_song.lyrics == Lyrics.empty()


def read_file(filename):
    file = open(filename, 'r')
    return file.read()