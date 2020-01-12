import pytest
from lyrics_mixer.title_parsers import ArtistsSplitter
from songs.model import SongTitle


@pytest.fixture
def splitter():
    return ArtistsSplitter()


def test_split_artists_enclosed_by_single_quote(splitter):
    results = splitter.split("mezcla 'Divididos' y 'Las Pelotas'")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_first_artist_enclosed_by_single_quote_and_second_artist_enclosed_by_double_quote(splitter):
    results = splitter.split("mezcla 'Divididos' y \"Las Pelotas\"")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_first_artist_enclosed_by_double_quote_and_second_artist_enclosed_by_single_quote(splitter):
    results = splitter.split("mezcla \"Divididos\" y 'Las Pelotas'")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_enclosed_by_different_quotes_before_and_after(splitter):
    results = splitter.split("mezcla \"Divididos' y 'Las Pelotas\"")
    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_enclosed_by_double_quote(splitter):
    results = splitter.split('mezcla "Divididos" y "Las Pelotas"')
    assert results == ['Divididos', 'Las Pelotas']
