import pytest
from unittest.mock import Mock

import songs.tests.song_factory as song_factory
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix

line_interleave_mix = LineInterleaveLyricsMix()

@pytest.fixture
def lyrics_mixer(mock_lyrics_library, lyrics_mix):
    return LyricsMixer(mock_lyrics_library, lyrics_mix)

@pytest.fixture
def mock_lyrics_library():
    return Mock()

@pytest.fixture
def lyrics_mix():
    return line_interleave_mix

@pytest.fixture
def mixed_lyrics():
    song1 = song_factory.create_stairway_to_heaven()
    song2 = song_factory.create_born_to_be_wild() 
    return line_interleave_mix.mix(song1, song2)