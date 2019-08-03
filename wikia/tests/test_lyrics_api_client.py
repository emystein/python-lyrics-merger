import pytest
from lyrics_merger.song import SongTitle
from wikia.lyrics_api_client import WikiaLyricsApiClient
import lyricwikia


@pytest.fixture
def lyrics_api_client():
    return WikiaLyricsApiClient()


def test_get_song(lyrics_api_client):
    song = lyrics_api_client.get_song(SongTitle('Led Zeppelin', 'Stairway To Heaven'))
    assert song.lyrics.text == lyricwikia.get_lyrics('Led Zeppelin', 'Stairway To Heaven')


def test_get_random_song(lyrics_api_client):
    song = lyrics_api_client.get_random_song()
    assert song.lyrics.text != ''


def test_get_random_song_by_artist(lyrics_api_client):
    song = lyrics_api_client.get_random_song_by_artist('Led Zeppelin')
    assert song.title.artist == 'Led Zeppelin'
    assert song.title.title != ''
    assert song.lyrics.text != ''
