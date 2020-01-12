import pytest
from lyrics_mixer.title_parsers import ArtistsSplitter
from songs.model import SongTitle


@pytest.fixture
def splitter():
    return ArtistsSplitter()


def test_split_artists_connector_y(splitter):
    results = splitter.split("Divididos y Las Pelotas")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_connector_and(splitter):
    results = splitter.split("Divididos and Las Pelotas")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_connector_con(splitter):
    results = splitter.split("Divididos con Las Pelotas")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_connector_with(splitter):
    results = splitter.split("Divididos with Las Pelotas")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_fist_artist_name_contains_connector(splitter):
    results = splitter.split(
        "mezcla Patricio Rey y sus redonditos de ricotta y Sumo")
    assert results == [
        'Patricio Rey y sus redonditos de ricotta', 'Sumo']


def test_split_artists_second_artist_name_contains_connector(splitter):
    results = splitter.split(
        "mezcla Sumo y 'Patricio Rey y sus redonditos de ricotta'")
    assert results == [
        'Sumo', 'Patricio Rey y sus redonditos de ricotta']
