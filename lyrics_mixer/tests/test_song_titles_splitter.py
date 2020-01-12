import pytest
from lyrics_mixer.song_titles_parser import SongTitlesSplitter
from songs.model import SongTitle


@pytest.fixture
def splitter():
    return SongTitlesSplitter()


prefixes = ['', 'mezclá ', 'combiná ', 'mix ',
            '@lyricsmixer mezclá ', 'Homer Simpson mezclá ']


connectors = [', ', ' y ', ' and ', ' con ', ' with ']


@pytest.mark.parametrize('prefix', prefixes)
@pytest.mark.parametrize('connector', connectors)
def test_split_artists_by_connector(splitter, prefix, connector):
    results = splitter.split(f"{prefix}Divididos{connector}Las Pelotas")
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
