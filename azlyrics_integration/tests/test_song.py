import pytest
from azlyrics_integration.model import Song
from songs.model import Lyrics
from songs.tests.fixtures.song_titles import song_title1


@pytest.mark.slow_integration_test
def test_get_song(song_title1):
    song = Song.entitled(song_title1)

    assert song.has_lyrics()

