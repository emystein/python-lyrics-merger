import pytest
from lyrics_mixer.artists_parser import ArtistsParser
from lyrics_mixer.song import SongTitle

@pytest.fixture
def parser():
    return ArtistsParser()


def test_parse_artists(parser):
    parse_results = parser.parse("mezclá Divididos y Las Pelotas")
    assert parse_results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_prefix_combiná(parser):
    parse_results = parser.parse("combiná Divididos y Las Pelotas")
    assert parse_results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_enclosed_by_single_quote(parser):
    parse_results = parser.parse("mezcla 'Divididos' y 'Las Pelotas'")
    assert parse_results.artists == ['Divididos', 'Las Pelotas']


def test_parse_first_artist_enclosed_by_single_quote_and_second_artist_enclosed_by_double_quote(parser):
    parse_results = parser.parse("mezcla 'Divididos' y \"Las Pelotas\"")
    assert parse_results.artists == ['Divididos', 'Las Pelotas']


def test_parse_first_artist_enclosed_by_double_quote_and_second_artist_enclosed_by_single_quote(parser):
    parse_results = parser.parse("mezcla \"Divididos\" y 'Las Pelotas'")
    assert parse_results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_enclosed_by_different_quotes_before_and_after(parser):
    parse_results = parser.parse("mezcla \"Divididos' y 'Las Pelotas\"")
    assert parse_results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_enclosed_by_double_quote(parser):
    parse_results = parser.parse('mezcla "Divididos" y "Las Pelotas"')
    assert parse_results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_fist_artist_name_contains_y(parser):
    parse_results = parser.parse("mezcla Patricio Rey y sus redonditos de ricotta y Sumo")
    assert parse_results.artists == ['Patricio Rey y sus redonditos de ricotta', 'Sumo']


def test_parse_artists_second_artist_name_contains_y(parser):
    parse_results = parser.parse("mezcla Sumo y 'Patricio Rey y sus redonditos de ricotta'")
    assert parse_results.artists == ['Sumo', 'Patricio Rey y sus redonditos de ricotta']


def test_parse_artists_english(parser):
    parse_results = parser.parse("mix Led Zeppelin and Steppenwolf")
    assert parse_results.artists == ['Led Zeppelin', 'Steppenwolf']

