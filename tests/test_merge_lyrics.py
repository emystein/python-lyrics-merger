import pytest
from lyrics_merger.song import SongTitle
from lyrics_merger.lyrics_merge import LyricsMerger, InterleaveParagraphsLyricsEditor, EmptyMergedLyrics
from wikia.lyrics_api_client import WikiaLyricsApiClient

@pytest.fixture
def lyrics_merger():
    return LyricsMerger(WikiaLyricsApiClient(), InterleaveParagraphsLyricsEditor())


# TODO mock WikiaLyricsApiClient and InterleaveParagraphsLyricsEditor
def test_merge_two_random_lyrics(lyrics_merger):
    merged_lyrics = lyrics_merger.merge_two_random_lyrics()
    assert merged_lyrics != EmptyMergedLyrics() 

def test_merge_random_lyrics_by_artists(lyrics_merger):
    merged_lyrics = lyrics_merger.merge_random_lyrics_by_artists('Led Zeppelin', 'Steppenwolf')
    assert merged_lyrics != EmptyMergedLyrics() 

def test_merge_two_specific_lyrics(lyrics_merger):
    song_title1 = SongTitle('Led Zeppelin', 'Stairway to Heaven')
    song_title2 = SongTitle('Steppenwolf', 'Born to be wild')
    merged_lyrics = lyrics_merger.merge_two_specific_lyrics(song_title1, song_title2)
    assert merged_lyrics.title == str(song_title1) + ', ' + str(song_title2) 
    assert merged_lyrics.text != ''