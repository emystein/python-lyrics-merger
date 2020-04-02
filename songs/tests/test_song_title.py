import pytest
from songs.model import SongTitle, EmptySongTitle, ArtistOnlySongTitle
import songs.tests.song_title_factory
from songs.tests.fixtures.song_titles import song_title1, song_title2

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


@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_song_title_not_equals_non_empty_artist_and_title(song_title1, song_title2):
    assert song_title1 != song_title2


def test_song_title_to_string(song_title1):
	assert song_title1.__str__() == 'Led Zeppelin - Stairway to Heaven'


def test_empty_song_title_eq():
    assert EmptySongTitle() == EmptySongTitle()


def test_empty_song_str():
    assert EmptySongTitle().__str__() == 'Empty Song Title'


def test_artist_only_song_title():
    song_title = ArtistOnlySongTitle('Led Zeppelin')

    assert song_title.artist == 'Led Zeppelin'
    assert song_title.title ==  None


def test_artist_only_song_title_eq():
    led_zeppelin = ArtistOnlySongTitle('Led Zeppelin')
    assert led_zeppelin == led_zeppelin
    assert led_zeppelin != ArtistOnlySongTitle('Steppenwolf')
    assert led_zeppelin != SongTitle('Led Zeppelin', 'Stairway to Heaven')
