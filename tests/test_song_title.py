import pytest
from lyrics_mixer.song import SongTitle
import tests.song_title_factory

@pytest.fixture
def song_title1():
    return tests.song_title_factory.create_stairway_to_heaven()

@pytest.fixture
def song_title2():
    return tests.song_title_factory.create_born_to_be_wild()

def test_strip_artist_and_title():
    song_title = SongTitle('  Led Zeppelin  ', '  Stairway to Heaven  ')
    assert song_title.artist == 'Led Zeppelin'
    assert song_title.title == 'Stairway to Heaven' 

def test_song_title_equals_empty_artist_and_title():
    song_title1 = SongTitle('', '')
    song_title2 = SongTitle('', '')
    assert song_title1 == song_title2


def test_song_title_equals_non_empty_artist_and_title(song_title1):
    song_title2 = SongTitle(song_title1.artist, song_title1.title)
    assert song_title1 == song_title2


def test_song_title_not_equals_non_empty_artist_and_title(song_title1, song_title2):
    assert song_title1 != song_title2


def test_song_title_to_string(song_title1):
	assert song_title1.__str__() == 'Led Zeppelin - Stairway to Heaven'