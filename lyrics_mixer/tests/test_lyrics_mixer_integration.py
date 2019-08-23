import pytest
from songs.model import SongTitle
from lyrics_mixer.dispatcher import Dispatcher
from lyrics_mixer.mixed_lyrics import EmptyMixedLyrics
from lyrics_mixer.lyrics_mix_strategies import ParagraphInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient
from songs.tests.fixtures.song_titles import song_title1, song_title2


@pytest.fixture
def lyrics_mixer():
    return Dispatcher(WikiaLyricsApiClient(), ParagraphInterleaveLyricsMix())


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