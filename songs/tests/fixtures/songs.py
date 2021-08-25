import pytest
import songs.tests.song_factory
from songs.model import SongTitle


stairway_to_heaven_title = SongTitle('Led Zeppelin', 'Stairway to Heaven')

born_to_be_wild_title = SongTitle('Steppenwolf', 'Born to be wild')


@pytest.fixture
def stairway_to_heaven():
	return songs.tests.song_factory.create_stairway_to_heaven()


@pytest.fixture
def born_to_be_wild():
	return songs.tests.song_factory.create_born_to_be_wild()


@pytest.fixture
def stairway_to_heaven_title():
	return stairway_to_heaven_title


@pytest.fixture
def born_to_be_wild_title():
	return born_to_be_wild_title
