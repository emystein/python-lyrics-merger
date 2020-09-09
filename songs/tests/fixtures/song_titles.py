import pytest
from songs.model import SongTitle

@pytest.fixture
def song_title1():
    return SongTitle('Led Zeppelin', 'Stairway to Heaven')


@pytest.fixture
def song_title2():
    return SongTitle('Steppenwolf', 'Born to be wild')