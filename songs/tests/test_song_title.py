import pytest
from songs.model import SongTitle
from songs.tests.fixtures.song_titles import song_title1, song_title2


def test_strip_artist_and_title(song_title1):
    assert SongTitle(f"  {song_title1.artist}  ", f"  {song_title1.title}  ") == song_title1


def test_song_title_equals_empty_artist_and_title():
    assert SongTitle('', '') == SongTitle('', '')


def test_song_title_equals_non_empty_artist_and_title(song_title1):
    assert SongTitle(song_title1.artist, song_title1.title) == song_title1


def test_song_title_not_equals_non_empty_artist_and_title(song_title1, song_title2):
    assert song_title1 != song_title2


def test_song_title_to_string(song_title1):
    assert song_title1.__str__() == f"{song_title1.artist} - {song_title1.title}"


def test_artist_only_song_title():
    song_title = SongTitle.artist_only('Led Zeppelin')

    assert song_title.artist == 'Led Zeppelin'
    assert song_title.title == ''
