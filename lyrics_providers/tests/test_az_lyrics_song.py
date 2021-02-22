import pytest

from lyrics_providers.azlyrics import Song


@pytest.mark.slow_integration_test
@pytest.mark.vcr()
def test_get_song():
    song = Song.entitled('Led Zeppelin', 'Stairway to Heaven')

    assert song.has_lyrics()

