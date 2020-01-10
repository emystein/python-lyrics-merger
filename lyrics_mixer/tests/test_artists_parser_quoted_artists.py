import pytest
from lyrics_mixer.title_parsers import ArtistsParser
from songs.model import SongTitle


@pytest.fixture
def parser():
    return ArtistsParser()


def test_parse_artists_enclosed_by_single_quote(parser):
    results = parser.parse("mezcla 'Divididos' y 'Las Pelotas'")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_first_artist_enclosed_by_single_quote_and_second_artist_enclosed_by_double_quote(parser):
    results = parser.parse("mezcla 'Divididos' y \"Las Pelotas\"")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_first_artist_enclosed_by_double_quote_and_second_artist_enclosed_by_single_quote(parser):
    results = parser.parse("mezcla \"Divididos\" y 'Las Pelotas'")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_enclosed_by_different_quotes_before_and_after(parser):
    results = parser.parse("mezcla \"Divididos' y 'Las Pelotas\"")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_enclosed_by_double_quote(parser):
    results = parser.parse('mezcla "Divididos" y "Las Pelotas"')
    assert results.artists == ['Divididos', 'Las Pelotas']
