import pytest

from lyrics_providers.azlyrics import Song
from songs.model import SongTitle

@pytest.mark.slow_integration_test
@pytest.mark.vcr()
def test_get_song():
    song = Song.entitled(SongTitle('Led Zeppelin', 'Stairway to Heaven'))

    assert song.has_lyrics()

