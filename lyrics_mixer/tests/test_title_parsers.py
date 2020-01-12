import pytest
from lyrics_mixer.title_parsers import SongTitlesParser
from lyrics_mixer.mix_commands import SongTitlesMixCommand, ArtistsMixCommand
from songs.model import SongTitle
from songs.tests.fixtures.song_titles import song_title1, song_title2

parser = SongTitlesParser()
connectors = [', ', ' y ', ' and '] 


@pytest.mark.usefixtures('song_title1', 'song_title2')
@pytest.mark.parametrize('connector', connectors)
def test_parse_song_titles(song_title1, song_title2, connector):
    result = parser.parse(f"{song_title1}{connector}{song_title2}")
    assert result.song_titles == [song_title1, song_title2]


@pytest.mark.usefixtures('song_title1', 'song_title2')
@pytest.mark.parametrize('prefix', ['', '@lyricsmixer mezcla '])
@pytest.mark.parametrize('connector', connectors)
def test_parse_song_titles(song_title1, song_title2, prefix, connector):
    result = parser.parse(f"{prefix}{song_title1}{connector}{song_title2}")
    assert isinstance(result, SongTitlesMixCommand)


@pytest.mark.parametrize('connector', connectors)
def test_parse_artists_only(connector):
    result = parser.parse(f"Led Zeppelin{connector}Steppenwolf")
    assert isinstance(result, ArtistsMixCommand)
