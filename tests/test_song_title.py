import pytest
from app.song_title import SongTitle


def test_song_title_equals_empty_artist_and_title():
    song_title1 = SongTitle('', '')
    song_title2 = SongTitle('', '')
    assert song_title1 == song_title2


def test_song_title_equals_non_empty_artist_and_title():
    song_title1 = SongTitle('Led Zeppelin', 'Stairway to Heaven')
    song_title2 = SongTitle('Led Zeppelin', 'Stairway to Heaven')
    assert song_title1 == song_title2


def test_song_title_not_equals_non_empty_artist_and_title():
    song_title1 = SongTitle('Led Zeppelin', 'Stairway to Heaven')
    song_title2 = SongTitle('The Beatles', 'Tomorrow never knows')
    assert song_title1 != song_title2
