import pytest
from songs.model import SongTitle
from lyrics_mixer.lyrics_mixer import LyricsMixer, ParagraphInterleaveLyricsMix, EmptyMixedLyrics
from wikia.lyrics_api_client import WikiaLyricsApiClient
import tests.song_title_factory
from tests.fixtures.song_titles import song_title1, song_title2


@pytest.fixture
def lyrics_mixer():
    return LyricsMixer(WikiaLyricsApiClient(), ParagraphInterleaveLyricsMix())


# TODO mock WikiaLyricsApiClient and ParagraphInterleaveLyricsMix
def test_mix_two_random_lyrics(lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    assert mixed_lyrics != EmptyMixedLyrics() 

def test_mix_random_lyrics_by_artists(lyrics_mixer):
    mixed_lyrics = lyrics_mixer.mix_random_lyrics_by_artists('Led Zeppelin', 'Steppenwolf')
    assert mixed_lyrics != EmptyMixedLyrics() 

@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_mix_two_specific_lyrics(lyrics_mixer, song_title1, song_title2):
    mixed_lyrics = lyrics_mixer.mix_two_specific_lyrics(song_title1, song_title2)
    assert mixed_lyrics.title == str(song_title1) + ', ' + str(song_title2) 
    assert mixed_lyrics.text != ''