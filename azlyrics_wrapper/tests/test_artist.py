import pytest
from azlyrics_wrapper.model import Artist
from songs.model import SongTitle, Song, Lyrics
from songs.tests.fixtures.song_titles import song_title1, song_title2


def test_random_initial():
    allowed_letters = list('abcdefghijklmnopqrstuvwxyz#')

    initial = Artist.random_initial()

    assert initial in allowed_letters


def test_random():
    artist = Artist.random()

    assert artist.name != ''
    assert len(artist.all_songs()) > 0


def test_named_last_name_then_first_name():
    artist = Artist.named('Villere, Zack')

    assert artist.name == 'Zack Villere'


# @pytest.mark.vcr()
def test_get_all_songs_by_artist():
    assert len(Artist.named('Led Zeppelin').all_songs()) == 86


def test_get_random_song_by_artist():
    song = Artist.named('Led Zeppelin').random_song()

    assert song.artist == 'Led Zeppelin'
    assert song.title != SongTitle.empty()
    assert song.has_lyrics()


# @pytest.mark.vcr()
def test_lyrics_not_found():
    assert Artist.named('Menéndez').random_song().is_empty()
