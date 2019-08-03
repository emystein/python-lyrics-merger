import pytest
from lyrics_mixer.song import SongTitle
from lyrics_mixer.lyrics_mixer import LyricsMixer, ParagraphInterleaveLyricsEditor, EmptyMixedLyrics
from wikia.lyrics_api_client import WikiaLyricsApiClient

@pytest.fixture
def lyrics_mixer():
    return LyricsMixer(WikiaLyricsApiClient(), ParagraphInterleaveLyricsEditor())


# TODO mock WikiaLyricsApiClient and ParagraphInterleaveLyricsEditor
def test_mix_two_random_lyrics(lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    assert mixed_lyrics != EmptyMixedLyrics() 

def test_mix_random_lyrics_by_artists(lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_random_lyrics_by_artists('Led Zeppelin', 'Steppenwolf')
    assert mixed_lyrics != EmptyMixedLyrics() 

def test_mix_two_specific_lyrics(lyrics_mixer):
    song_title1 = SongTitle('Led Zeppelin', 'Stairway to Heaven')
    song_title2 = SongTitle('Steppenwolf', 'Born to be wild')
    mixed_lyrics = lyrics_mixer.mix_two_specific_lyrics(song_title1, song_title2)
    assert mixed_lyrics.title == str(song_title1) + ', ' + str(song_title2) 
    assert mixed_lyrics.text != ''