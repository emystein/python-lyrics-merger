import pytest
from lyrics_mixer.title_parsers import ArtistsParser
from songs.model import SongTitle


@pytest.fixture
def parser():
    return ArtistsParser()


def test_parse_artists_prefix_mezclá(parser):
    results = parser.parse("mezclá Divididos y Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_prefix_combiná(parser):
    results = parser.parse("combiná Divididos y Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_prefix_tweeter_username(parser):
    results = parser.parse("@lyricsmixer mezclá Divididos y Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_prefix_anything_before_mezclá(parser):
    results = parser.parse("Homero Simpson mezclá Divididos y Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']
