import pytest
import songs.tests.song_factory


@pytest.fixture
def song1():
	return songs.tests.song_factory.create_stairway_to_heaven()


@pytest.fixture
def song2():
	return songs.tests.song_factory.create_born_to_be_wild()