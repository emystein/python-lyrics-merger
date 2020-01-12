import pytest
from songs.model import SongTitle, NullSong, InstrumentalSong
import wikia.lyrics_api_client
from wikia.lyrics_api_client import WikiaLyricsApiClient
import lyricwikia
from songs.tests.fixtures.song_titles import song_title1, song_title2


@pytest.fixture
def lyrics_library():
    return WikiaLyricsApiClient()


@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_get_song(lyrics_library, song_title1):
    song = lyrics_library.get_song(song_title1)
    assert song.lyrics.text == lyricwikia.get_lyrics(song_title1.artist, song_title1.title)


@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_get_songs(lyrics_library, song_title1, song_title2):
    songs = lyrics_library.get_songs([song_title1, song_title2])
    expected = [lyricwikia.get_lyrics(song_title1.artist, song_title1.title), 
                lyricwikia.get_lyrics(song_title2.artist, song_title2.title)]
    assert len(songs) == 2
    for song in songs:
        assert song.lyrics.text in expected


def test_get_all_songs_by_artist():
    all_songs = wikia.lyrics_api_client.find_all_songs_by_artist('Led Zeppelin')
    assert len(all_songs) == 156


def test_get_random_song(lyrics_library):
    song = lyrics_library.get_random_song()
    assert song.lyrics.text != ''


def test_get_random_songs(lyrics_library):
    songs = lyrics_library.get_random_songs(2)
    assert len(songs) == 2
    for song in songs:
        assert song.lyrics.text != ''


def test_get_random_song_by_artist(lyrics_library):
    song = lyrics_library.get_random_song_by_artist('Led Zeppelin')
    assert song.title.artist == 'Led Zeppelin'
    assert song.title.title != ''
    assert song.lyrics.text != ''


def test_get_random_songs_by_artists(lyrics_library):
    songs = lyrics_library.get_random_songs_by_artists(['Madonna', 'Slayer'])
    assert len(songs) == 2
    for song in songs:
        assert song.title.artist == 'Madonna' or song.title.artist == 'Slayer'
        assert song.title.title != ''
        assert song.lyrics.text != ''


def test_lyrics_not_found(lyrics_library):
    assert lyrics_library.get_random_song_by_artist('Emiliano Menéndez') == NullSong()


def test_instrumental_song(lyrics_library):
    song_title = SongTitle('Deep Forest', 'Boheme')
    assert lyrics_library.get_song(song_title) == InstrumentalSong('Deep Forest', 'Boheme')
