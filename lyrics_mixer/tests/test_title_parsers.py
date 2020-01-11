import pytest
from lyrics_mixer.title_parsers import SongTitlesParser
from songs.model import SongTitle
from songs.tests.fixtures.song_titles import song_title1, song_title2

parser = SongTitlesParser()

separators = [', ', ' y ', ' and ']


@pytest.mark.usefixtures('song_title1', 'song_title2')
@pytest.mark.parametrize('prefix', ['', '@lyricsmixer mezcla '])
@pytest.mark.parametrize('separator', separators)
def test_parse_song_titles(song_title1, song_title2, prefix, separator):
    result = parser.parse(f"{prefix}{song_title1}{separator}{song_title2}")
    assert result.song_titles == [song_title1, song_title2]


@pytest.mark.parametrize('separator', separators)
def test_parse_artists_only(separator):
    result = parser.parse(f"Led Zeppelin{separator}Steppenwolf")
    assert result.artists == ['Led Zeppelin', 'Steppenwolf']
