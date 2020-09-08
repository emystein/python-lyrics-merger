import pytest
from lyrics_mixer.song_titles_parser import SongTitlesSplitter
from songs.model import SongTitle


splitter = SongTitlesSplitter()


def test_split_artists_enclosed_by_single_quote():
    results = splitter.split("mezcla 'Divididos' y 'Las Pelotas'")

    assert results == ['Divididos', 'Las Pelotas']


def test_split_first_artist_enclosed_by_single_quote_and_second_artist_enclosed_by_double_quote():
    results = splitter.split("mezcla 'Divididos' y \"Las Pelotas\"")

    assert results == ['Divididos', 'Las Pelotas']


def test_split_first_artist_enclosed_by_double_quote_and_second_artist_enclosed_by_single_quote():
    results = splitter.split("mezcla \"Divididos\" y 'Las Pelotas'")

    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_enclosed_by_different_quotes_before_and_after():
    results = splitter.split("mezcla \"Divididos' y 'Las Pelotas\"")

    assert results == ['Divididos', 'Las Pelotas']


def test_split_artists_enclosed_by_double_quote():
    results = splitter.split('mezcla "Divididos" y "Las Pelotas"')

    assert results == ['Divididos', 'Las Pelotas']
