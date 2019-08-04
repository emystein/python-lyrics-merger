import pytest
from lyrics_mixer.song import SongTitle
from wikia.lyrics_api_client import WikiaLyricsApiClient
import lyricwikia


@pytest.fixture
def lyrics_api_client():
    return WikiaLyricsApiClient()


def test_get_song(lyrics_api_client):
    song = lyrics_api_client.get_song(SongTitle('Led Zeppelin', 'Stairway To Heaven'))
    assert song.lyrics.text == lyricwikia.get_lyrics('Led Zeppelin', 'Stairway To Heaven')


def test_get_songs(lyrics_api_client):
    songs = lyrics_api_client.get_songs([SongTitle('Led Zeppelin', 'Stairway To Heaven'), SongTitle('Steppenwolf', 'Born to be wild')])
    expected = [lyricwikia.get_lyrics('Led Zeppelin', 'Stairway To Heaven'), lyricwikia.get_lyrics('Steppenwolf', 'Born to be wild')]
    assert len(songs) == 2
    for song in songs:
        assert song.lyrics.text in expected


def test_get_all_songs_by_artist(lyrics_api_client):
    all_songs = lyrics_api_client.find_all_songs_by_artist('Led Zeppelin')
    assert len(all_songs) == 156


def test_get_random_song(lyrics_api_client):
    song = lyrics_api_client.get_random_song()
    assert song.lyrics.text != ''


def test_get_random_songs(lyrics_api_client):
    songs = lyrics_api_client.get_random_songs(2)
    assert len(songs) == 2
    for song in songs:
        assert song.lyrics.text != ''


def test_get_random_song_by_artist(lyrics_api_client):
    song = lyrics_api_client.get_random_song_by_artist('Led Zeppelin')
    assert song.title.artist == 'Led Zeppelin'
    assert song.title.title != ''
    assert song.lyrics.text != ''


def test_get_random_songs_by_artists(lyrics_api_client):
    songs = lyrics_api_client.get_random_songs_by_artists(['Led Zeppelin', 'Steppenwolf'])
    assert len(songs) == 2
    for song in songs:
        assert song.title.artist == 'Led Zeppelin' or song.title.artist == 'Steppenwolf'
        assert song.title.title != ''
        assert song.lyrics.text != ''
