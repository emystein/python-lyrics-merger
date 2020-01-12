import pytest
from lyrics_mixer.title_parsers import ArtistsSplitter
from songs.model import SongTitle


@pytest.fixture
def splitr():
    return ArtistsSplitter()


def test_split_artists_prefix_mezclá(splitr):
    results = splitr.split("mezclá Divididos y Las Pelotas")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_prefix_combiná(splitr):
    results = splitr.split("combiná Divididos y Las Pelotas")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_prefix_tweeter_username(splitr):
    results = splitr.split("@lyricsmixer mezclá Divididos y Las Pelotas")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_prefix_anything_before_mezclá(splitr):
    results = splitr.split("Homero Simpson mezclá Divididos y Las Pelotas")
    assert results == ['Divididos', 'Las Pelotas']
