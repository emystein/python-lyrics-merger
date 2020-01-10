import pytest
from lyrics_mixer.title_parsers import ArtistsParser
from songs.model import SongTitle


@pytest.fixture
def parser():
    return ArtistsParser()


def test_parse_artists_connector_y(parser):
    results = parser.parse("Divididos y Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_connector_and(parser):
    results = parser.parse("Divididos and Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_connector_con(parser):
    results = parser.parse("Divididos con Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_connector_with(parser):
    results = parser.parse("Divididos with Las Pelotas")
    assert results.artists == ['Divididos', 'Las Pelotas']


def test_parse_artists_fist_artist_name_contains_connector(parser):
    results = parser.parse(
        "mezcla Patricio Rey y sus redonditos de ricotta y Sumo")
    assert results.artists == [
        'Patricio Rey y sus redonditos de ricotta', 'Sumo']


def test_parse_artists_second_artist_name_contains_connector(parser):
    results = parser.parse(
        "mezcla Sumo y 'Patricio Rey y sus redonditos de ricotta'")
    assert results.artists == [
        'Sumo', 'Patricio Rey y sus redonditos de ricotta']
