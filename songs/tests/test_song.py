from songs.model import Song, Lyrics


def test_song_equals_by_artist_and_title():
    song1 = Song('Led Zeppelin', 'Stairway to Heaven', Lyrics('some lyrics'))
    song2 = Song('Led Zeppelin', 'Stairway to Heaven', Lyrics('other lyrics'))
    assert song1 == song2


def test_none_song():
    none_song = Song.none()
    assert none_song.artist == ''
    assert none_song.title == ''
    assert none_song.lyrics == Lyrics.empty()

