import pytest

import songs.tests.song_factory as song_factory
from lyrics_mixer.lyrics_mixer import LineInterleaveLyricsMix

line_interleave_mix = LineInterleaveLyricsMix()


@pytest.fixture
def lyrics_mix():
    return line_interleave_mix


@pytest.fixture
def mixed_lyrics():
    stairway_to_heaven = song_factory.create_stairway_to_heaven()
    born_to_be_wild = song_factory.create_born_to_be_wild()
    return line_interleave_mix.mix(stairway_to_heaven, born_to_be_wild)
