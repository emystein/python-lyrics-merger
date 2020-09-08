import pytest
from lyrics_mixer.song_titles_parser import SongTitlesSplitter
from songs.model import SongTitle


prefixes = SongTitlesSplitter.prefixes() + ['@lyricsmixer mezclá ', 'Fulano mezclá ']

splitter = SongTitlesSplitter()


@pytest.mark.parametrize('prefix', prefixes)
@pytest.mark.parametrize('connector', SongTitlesSplitter.connectors())
@pytest.mark.parametrize('title1, title2',
                         [
                             ('Divididos', 'Las Pelotas'),
                             ('Patricio Rey y sus redonditos de ricotta', 'Sumo'),
                             ('Led Zeppelin - Stairway to Heaven', 'Steppenwolf - Born to be wild')
                         ])
def test_split_artists_by_connector(prefix, connector, title1, title2):
    results = splitter.split(f"{prefix}{title1}{connector}{title2}") 
    
    assert results == [title1, title2]


def test_split_artists_second_artist_name_contains_connector():
    results = splitter.split(
        "mezclá Sumo y 'Patricio Rey y sus redonditos de ricotta'")

    assert results == ['Sumo', 'Patricio Rey y sus redonditos de ricotta']


@pytest.mark.parametrize("full_title", [
    ("'Divididos y Las Pelotas'"),
    ("'Divididos' y \"Las Pelotas\""),
    ("\"Divididos\" y 'Las Pelotas'"),
    ("\"Divididos' y 'Las Pelotas\""),
    ("\"Divididos\" y \"Las Pelotas\""),
])
def test_split_artists_quoted(full_title):
    results = splitter.split(f"mezcla {full_title}")

    assert results == ['Divididos', 'Las Pelotas']
