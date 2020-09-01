import pytest
from songs.model import SongTitle, NullSong, Song, Lyrics, EmptyLyrics
from wikia.lyrics_api_client import WikiaLyricsApiClient
import lyricwikia
from songs.tests.fixtures.song_titles import song_title1, song_title2


@pytest.fixture
def lyrics_library():
    return WikiaLyricsApiClient()


@pytest.mark.usefixtures('song_title1')
def test_get_song(lyrics_library, song_title1):
    song = lyrics_library.get_song(song_title1)

    assert song.lyrics == Lyrics(lyricwikia.get_lyrics(song_title1.artist, song_title1.title))


@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_get_songs(lyrics_library, song_title1, song_title2):
    song_titles = [song_title1, song_title2]

    songs = lyrics_library.get_songs(song_titles)

    assert len(songs) == len(song_titles)

    for song in songs:
        assert song.lyrics == Lyrics(lyricwikia.get_lyrics(song.artist, song.title))


def test_get_all_songs_by_artist(lyrics_library):
    all_songs = lyrics_library.find_all_songs_by_artist('Led Zeppelin')

    assert len(all_songs) == 156


def test_get_random_song(lyrics_library):
    song = lyrics_library.get_random_song()

    assert song.has_lyrics()


def test_get_random_songs(lyrics_library):
    songs = lyrics_library.get_random_songs(2)

    assert len(songs) == 2

    for song in songs:
        assert song.has_lyrics()


def test_get_random_song_by_artist(lyrics_library):
    song = lyrics_library.get_random_song_by_artist('Led Zeppelin')

    assert song.artist == 'Led Zeppelin'
    assert song.title != ''
    assert song.has_lyrics()


def test_get_random_songs_by_artists(lyrics_library):
    songs = lyrics_library.get_random_songs_by_artists(['Madonna', 'Slayer'])

    assert len(songs) == 2

    for song in songs:
        assert song.artist == 'Madonna' or song.artist == 'Slayer'
        assert song.title != ''
        assert song.has_lyrics()


def test_lyrics_not_found(lyrics_library):
    assert lyrics_library.get_random_song_by_artist('Menéndez') == NullSong()


def test_instrumental_song(lyrics_library):
    song = lyrics_library.get_song(SongTitle('Deep Forest', 'Boheme'))

    assert song == Song('Deep Forest', 'Boheme', 'Instrumental')
