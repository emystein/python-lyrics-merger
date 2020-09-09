import pytest
import lyricwikia
from wikia.lyrics_api_client import WikiaLyricsApiClient
from wikia.model import Song
from songs.model import SongTitle, Lyrics
from songs.tests.fixtures.song_titles import song_titles, song_title1, song_title2


@pytest.fixture
def library():
    return WikiaLyricsApiClient()


@pytest.mark.vcr()
@pytest.mark.usefixtures('song_title1')
def test_get_song(library, song_title1):
    song = Song.entitled(song_title1)

    assert song.lyrics == Lyrics(lyricwikia.get_lyrics(song_title1.artist, song_title1.title))


def test_get_random_songs(library):
    songs = library.get_random_songs(2)

    assert len(songs) == 2

    for song in songs:
        assert song.has_lyrics()


def test_get_random_songs_by_artists(library):
    artists = ['Madonna', 'Slayer'] 

    songs = library.get_random_songs_by_artists(artists)

    assert len(songs) == 2

    for song in songs:
        assert song.artist in artists 
        assert song.title != SongTitle.empty()
        assert song.has_lyrics()


@pytest.mark.vcr()
def test_instrumental_song(library):
    song = library.get_song(SongTitle('Deep Forest', 'Boheme'))

    assert song.artist == 'Deep Forest'
    assert song.title == SongTitle('Deep Forest', 'Boheme')
    assert song.lyrics == Lyrics('Instrumental')
