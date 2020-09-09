import pytest
import lyricwikia
from wikia.model import Song
from songs.model import Lyrics
from songs.tests.fixtures.song_titles import song_title1


@pytest.mark.vcr()
def test_get_song(song_title1):
    song = Song.entitled(song_title1)

    assert song.lyrics == Lyrics(lyricwikia.get_lyrics(song_title1.artist, song_title1.title))

