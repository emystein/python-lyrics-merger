import pytest
from lyrics_mixer.song_titles_parser import SongTitlesSplitter
from songs.model import SongTitle


prefixes = SongTitlesSplitter.prefixes() + ['@lyricsmixer mezclá ', 'Homer Simpson mezclá ']


@pytest.mark.parametrize('prefix', prefixes)
@pytest.mark.parametrize('connector', SongTitlesSplitter.connectors())
def test_split_artists_by_connector(prefix, connector):
    splitter = SongTitlesSplitter()
    
    results = splitter.split(f"{prefix}Divididos{connector}Las Pelotas")

    assert results == ['Divididos', 'Las Pelotas']


@pytest.mark.parametrize('prefix', prefixes)
@pytest.mark.parametrize('connector', SongTitlesSplitter.connectors())
def test_split_artists_fist_artist_name_contains_connector(prefix, connector):
    splitter = SongTitlesSplitter()

    results = splitter.split(
        f"{prefix}Patricio Rey y sus redonditos de ricotta{connector}Sumo")

    assert results == [
        'Patricio Rey y sus redonditos de ricotta', 'Sumo']


def test_split_artists_second_artist_name_contains_connector():
    splitter = SongTitlesSplitter()

    results = splitter.split(
        "mezcla Sumo y 'Patricio Rey y sus redonditos de ricotta'")

    assert results == [
        'Sumo', 'Patricio Rey y sus redonditos de ricotta']


@pytest.mark.parametrize('connector', SongTitlesSplitter.connectors())
def test_split_song_titles_containing_artist_and_song(connector):
    song_title1 = 'Led Zeppelin - Stairway to Heaven'
    song_title2 = 'Steppenwolf - Born to be wild'

    splitter = SongTitlesSplitter()
    results = splitter.split(f"{song_title1}{connector}{song_title2}")

    assert results == [song_title1, song_title2]
