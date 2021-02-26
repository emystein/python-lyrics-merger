from songs.model import SongTitle, Song, Lyrics


def test_song_equals_by_artist_and_title():
    song1 = Song(SongTitle('Led Zeppelin', 'Stairway to Heaven'), Lyrics('some lyrics'))
    song2 = Song(SongTitle('Led Zeppelin', 'Stairway to Heaven'), Lyrics('other lyrics'))
    assert song1 == song2


def test_none_song():
    none_song = Song.none()
    assert none_song.title.is_empty()
    assert none_song.lyrics == Lyrics.empty()

