import pytest

from songs.model import SongTitle
from lyrics_providers.azlyrics import AZLyricsLibrary
from lyrics_mixer.lyrics_mixer import LyricsMixer
from lyrics_mixer.tests.fixtures.mixer import lyrics_mix
from songs.tests.fixtures.songs import stairway_to_heaven_title, born_to_be_wild_title

@pytest.mark.slow_integration_test
def test_mix_two_random_lyrics_integration(lyrics_mix):
    mixer = LyricsMixer(AZLyricsLibrary(), lyrics_mix)

    mixed_lyrics = mixer.mix_two_random_lyrics()

    assert mixed_lyrics.has_content()


@pytest.mark.slow_integration_test
def test_mix_random_lyrics_by_artists_integration(lyrics_mix):
    mixer = LyricsMixer(AZLyricsLibrary(), lyrics_mix)

    mixed_lyrics = mixer.mix_random_lyrics_by_artists('Led Zeppelin', 'Steppenwolf')

    assert mixed_lyrics.has_content()


@pytest.mark.slow_integration_test
@pytest.mark.vcr()
def test_mix_specific_lyrics_integration(lyrics_mix):
    mixer = LyricsMixer(AZLyricsLibrary(), lyrics_mix)

    stairway_to_heaven_title = SongTitle('Led Zeppelin', 'Stairway to Heaven')
    born_to_be_wild_title = SongTitle('Steppenwolf', 'Born to be wild')

    mixed_lyrics = mixer.mix_specific_lyrics(stairway_to_heaven_title, born_to_be_wild_title)

    assert mixed_lyrics.has_content()
