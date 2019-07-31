import pytest
from app.random_lyrics_downloader import RandomLyricsDownloader
from app.song import SongTitle
from wikia.lyrics_api_client import WikiaLyricsApiClient


@pytest.fixture
def lyrics_downloader():
    return RandomLyricsDownloader(WikiaLyricsApiClient())


def test_get_random_lyrics_from_wikia(lyrics_downloader):
    song = lyrics_downloader.get_random()
    assert song.title != SongTitle('', '')
    assert song.lyrics.text != ''


def test_get_random_lyrics_by_artist_from_wikia(lyrics_downloader):
    song = lyrics_downloader.get_random_by_artist('Led Zeppelin')
    assert song.title.artist == 'Led Zeppelin'
    assert song.title.title != ''
    assert song.lyrics.text != ''
