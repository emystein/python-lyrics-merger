from songs.model import SongTitle, Song, Lyrics
from songs.tests.fixtures.songs import stairway_to_heaven_title


def test_song_equals_by_artist_and_title(stairway_to_heaven_title):
    song1 = Song(stairway_to_heaven_title, Lyrics.with_text('some lyrics'))
    song2 = Song(stairway_to_heaven_title, Lyrics.with_text('other lyrics'))
    assert song1 == song2


def test_none_song():
    song = Song.none()
    assert song.title.is_empty()
    assert song.lyrics == Lyrics.empty()

