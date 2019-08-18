import pytest
from lyrics_mixer.artists_parser import ArtistsParser
from songs.model import SongTitle

@pytest.fixture
def parser():
    return ArtistsParser()


def test_parse_artists(parser):
    results = parser.parse("Divididos y Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_prefix_mezclá(parser):
    results = parser.parse("mezclá Divididos y Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_prefix_combiná(parser):
    results = parser.parse("combiná Divididos y Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


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


def test_parse_artists_fist_artist_name_contains_y(parser):
    results = parser.parse("mezcla Patricio Rey y sus redonditos de ricotta y Sumo")
    assert results.artists == ['Patricio Rey y sus redonditos de ricotta', 'Sumo']


def test_parse_artists_second_artist_name_contains_y(parser):
    results = parser.parse("mezcla Sumo y 'Patricio Rey y sus redonditos de ricotta'")
    assert results.artists == ['Sumo', 'Patricio Rey y sus redonditos de ricotta']


def test_parse_artists_english(parser):
    results = parser.parse("mix Led Zeppelin and Steppenwolf")
    assert results.artists == ['Led Zeppelin', 'Steppenwolf']


def test_parse_artists_prefix_tweeter_username(parser):
    results = parser.parse("@lyricsmixer mezclá Divididos y Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_prefix_anything_before_mezclá(parser):
    results = parser.parse("Homero Simpson mezclá Divididos y Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']