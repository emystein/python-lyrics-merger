import pytest
from app.lyrics_merge import RandomLyricsMerger, LyricsEditor
from app.song_downloader import RandomSongDownloader
from wikia.lyrics_api_client import WikiaLyricsApiClient


# TODO mock RandomLyricsDownloader and LyricsEditor
def test_merge_two_random_lyrics():
    lyrics_downloader = RandomSongDownloader(WikiaLyricsApiClient())
    merger = RandomLyricsMerger(lyrics_downloader, LyricsEditor())
    merged_lyrics = merger.merge_two_random_lyrics()
    assert merged_lyrics.title != ''
    assert merged_lyrics.text != ''
