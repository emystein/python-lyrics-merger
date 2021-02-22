import pytest

from lyrics_mixer.lyrics_data_source import LyricsDataSource
from lyrics_mixer.lyrics_mixer import LyricsMixer
from lyrics_mixer.tests.fixtures.mixer import lyrics_mix

@pytest.mark.slow_integration_test
def test_mix_random_lyrics_by_artists_integration(lyrics_mix):
    mixer = LyricsMixer(LyricsDataSource(), lyrics_mix)

    mixed_lyrics = mixer.mix_random_lyrics_by_artists('Led Zeppelin', 'Steppenwolf')

    assert mixed_lyrics.has_content()


@pytest.mark.slow_integration_test
@pytest.mark.vcr()
def test_mix_two_specific_lyrics_integration(lyrics_mix):
    mixer = LyricsMixer(LyricsDataSource(), lyrics_mix)

    mixed_lyrics = mixer.mix_two_specific_lyrics('Led Zeppelin', 'Stairway to Heaven', 'Steppenwolf', 'Born to be wild')

    assert mixed_lyrics.has_content()
