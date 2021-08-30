import pytest

from songs.tests.song_factory import *
from lyrics_mixer.lyrics_mixer import LineInterleaveLyricsMix


@pytest.fixture
def mixed_lyrics():
    return LineInterleaveLyricsMix().mix(stairway_to_heaven_lyrics(),
                                         born_to_be_wild_lyrics())
