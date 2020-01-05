import pytest
from songs.model import SongTitle
from lyrics_mixer.lyrics_mixers import *
from lyrics_mixer.mixed_lyrics import EmptyMixedLyrics
from lyrics_mixer.lyrics_mix_strategies import ParagraphInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient
from songs.tests.fixtures.song_titles import song_title1, song_title2


@pytest.fixture
def lyrics_library():
    return WikiaLyricsApiClient()

@pytest.fixture
def lyrics_mix_strategy():
    return ParagraphInterleaveLyricsMix()


def test_mix_two_random_lyrics(lyrics_library, lyrics_mix_strategy):
    lyrics_mixer = RandomLyricsMixer(lyrics_library)
    mixed_lyrics = lyrics_mixer.mix_lyrics(lyrics_mix_strategy)

    assert mixed_lyrics != EmptyMixedLyrics() 

def test_mix_random_lyrics_by_artists(lyrics_library, lyrics_mix_strategy):
    lyrics_mixer = RandomByArtistsLyricsMixer(lyrics_library, 'Led Zeppelin', 'Steppenwolf')
    mixed_lyrics = lyrics_mixer.mix_lyrics(lyrics_mix_strategy)

    assert mixed_lyrics != EmptyMixedLyrics() 

@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_mix_two_specific_lyrics(lyrics_library, lyrics_mix_strategy, song_title1, song_title2):
    lyrics_mixer = SpecificLyricsMixer(lyrics_library, song_title1, song_title2)
    mixed_lyrics = lyrics_mixer.mix_lyrics(lyrics_mix_strategy)

    assert mixed_lyrics.title == str(song_title1) + ', ' + str(song_title2) 
    assert mixed_lyrics.text != ''