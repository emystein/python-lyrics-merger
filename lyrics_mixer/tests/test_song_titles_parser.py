import pytest
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser, ParsedSongTitles, ParsedArtists
from songs.model import SongTitle, EmptySongTitle, ArtistOnlySongTitle
from songs.tests.fixtures.song_titles import song_title1, song_title2

song_titles_parser = SongTitlesParser(SongTitlesSplitter())

connectors = [', ', ' y ', ' and ']


@pytest.mark.usefixtures('song_title1', 'song_title2')
@pytest.mark.parametrize('prefix', ['', '@lyricsmixer mezcla '])
@pytest.mark.parametrize('connector', connectors)
def test_parse_song_titles(song_title1, song_title2, prefix, connector):
    parsed = song_titles_parser.parse(f"{prefix}{song_title1}{connector}{song_title2}")

    assert parsed.song_title1 == song_title1
    assert parsed.song_title2 == song_title2


@pytest.mark.parametrize('connector', connectors)
def test_parse_artists_only(connector):
    parsed = song_titles_parser.parse(f"Led Zeppelin{connector}Steppenwolf")

    assert parsed.song_title1.artist == 'Led Zeppelin'
    assert parsed.song_title2.artist == 'Steppenwolf'


@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_parsed_song_titles(song_title1, song_title2):
    split_text = [song_title1.__str__(), song_title2.__str__()]

    parsed = ParsedSongTitles(split_text)

    assert parsed.song_title1 == song_title1
    assert parsed.song_title2 == song_title2


def test_parse_artists_only():
    split_text = ['Led Zeppelin', 'Steppenwolf']

    parsed = ParsedArtists(split_text)

    assert parsed.song_title1 == ArtistOnlySongTitle('Led Zeppelin')
    assert parsed.song_title2 == ArtistOnlySongTitle('Steppenwolf')
