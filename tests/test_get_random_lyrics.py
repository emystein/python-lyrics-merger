import pytest
from lyrics_merger.song_downloader import RandomSongDownloader
from wikia.lyrics_api_client import WikiaLyricsApiClient


@pytest.fixture
def song_downloader():
    return RandomSongDownloader(WikiaLyricsApiClient())


def test_get_random_song(song_downloader):
    song = song_downloader.get_random()
    assert song.title.artist != ''
    assert song.title.title != ''
    assert song.lyrics.text != ''


def test_get_random_song_by_artist(song_downloader):
    song = song_downloader.get_random_by_artist('Led Zeppelin')
    assert song.title.artist == 'Led Zeppelin'
    assert song.title.title != ''
    assert song.lyrics.text != ''
