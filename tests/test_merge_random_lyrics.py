import pytest
from lyrics_merger.lyrics_merge import RandomLyricsMerger, LyricsEditor
from lyrics_merger.song_downloader import SongDownloader
from wikia.lyrics_api_client import WikiaLyricsApiClient

@pytest.fixture
def lyrics_merger():
    lyrics_downloader = SongDownloader(WikiaLyricsApiClient())
    return RandomLyricsMerger(lyrics_downloader, LyricsEditor())


# TODO mock RandomLyricsDownloader and LyricsEditor
def test_merge_two_random_lyrics(lyrics_merger):
    merged_lyrics = lyrics_merger.merge_two_random_lyrics()
    assert merged_lyrics.title != ''
    assert merged_lyrics.text != ''

def test_merge_random_lyrics_by_artists(lyrics_merger):
    merged_lyrics = lyrics_merger.merge_random_lyrics_by_artists('Led Zeppelin', 'Steppenwolf')
    assert merged_lyrics.title != ''
    assert merged_lyrics.text != ''
