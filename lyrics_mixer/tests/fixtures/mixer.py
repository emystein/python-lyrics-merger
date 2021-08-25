import pytest

from songs.tests.song_factory import *
from lyrics_mixer.lyrics_mixer import LineInterleaveLyricsMix

line_interleave_mix = LineInterleaveLyricsMix()


@pytest.fixture
def lyrics_mix():
    return line_interleave_mix


@pytest.fixture
def mixed_lyrics():
    return line_interleave_mix.mix(create_stairway_to_heaven(), create_born_to_be_wild())
