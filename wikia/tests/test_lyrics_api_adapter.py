import pytest
from wikia.lyrics_api_adapter import WikiaLyricsApiClient
import lyricwikia


@pytest.fixture
def lyrics_api_adapter():
    return WikiaLyricsApiClient()


def test_get_lyrics(lyrics_api_adapter):
    remote_song = lyrics_api_adapter.get_song('Led Zeppelin', 'Stairway To Heaven')
    assert remote_song.lyrics == lyricwikia.get_lyrics('Led Zeppelin', 'Stairway To Heaven')


def test_get_random_lyrics(lyrics_api_adapter):
    remote_song = lyrics_api_adapter.get_random_song()
    assert remote_song.lyrics != ''
