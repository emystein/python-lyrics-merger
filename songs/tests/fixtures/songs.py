import pytest
import songs.tests.song_factory as song_factory


@pytest.fixture
def stairway_to_heaven():
	return song_factory.stairway_to_heaven()


@pytest.fixture
def born_to_be_wild():
	return song_factory.born_to_be_wild()


@pytest.fixture
def stairway_to_heaven_title():
	return song_factory.stairway_to_heaven_title()


@pytest.fixture
def born_to_be_wild_title():
	return song_factory.born_to_be_wild_title()
