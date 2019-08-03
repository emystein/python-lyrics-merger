import pytest
from lyrics_mixer.song import SongTitle
from lyrics_mixer.lyrics_mixer import LyricsMixer, ParagraphInterleaveLyricsEditor, EmptyMixedLyrics
from wikia.lyrics_api_client import WikiaLyricsApiClient

@pytest.fixture
def lyrics_mixer():
    return LyricsMixer(WikiaLyricsApiClient(), ParagraphInterleaveLyricsEditor())


# TODO mock WikiaLyricsApiClient and ParagraphInterleaveLyricsEditor
def test_merge_two_random_lyrics(lyrics_mixer):
    merged_lyrics = lyrics_mixer.merge_two_random_lyrics()
    assert merged_lyrics != EmptyMixedLyrics() 

def test_merge_random_lyrics_by_artists(lyrics_mixer):
    merged_lyrics = lyrics_mixer.merge_random_lyrics_by_artists('Led Zeppelin', 'Steppenwolf')
    assert merged_lyrics != EmptyMixedLyrics() 

def test_merge_two_specific_lyrics(lyrics_mixer):
    song_title1 = SongTitle('Led Zeppelin', 'Stairway to Heaven')
    song_title2 = SongTitle('Steppenwolf', 'Born to be wild')
    merged_lyrics = lyrics_mixer.merge_two_specific_lyrics(song_title1, song_title2)
    assert merged_lyrics.title == str(song_title1) + ', ' + str(song_title2) 
    assert merged_lyrics.text != ''