import pytest
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser, FullTitlesParser, ArtistsParser
from songs.model import SongTitle, ArtistTitle
from songs.tests.fixtures.song_titles import song_title1, song_title2
from lyrics_mixer.tests.fixtures.mixer import mixer


@pytest.mark.parametrize('prefix', ['', '@lyricsmixer mezclá '])
@pytest.mark.parametrize('connector', [', ', ' y ', ' and '])
@pytest.mark.parametrize(
    'text1, text2, artist1, title1, artist2, title2',
    [
        ('Led Zeppelin - Stairway to Heaven', 'Steppenwolf - Born to be wild',
         'Led Zeppelin', 'Stairway to Heaven', 'Steppenwolf', 'Born to be wild'),
        ('U2', 'INXS', 'U2', '', 'INXS', '')
    ]
)
def test_parse_song_titles(prefix, connector, text1, text2, artist1, title1, artist2, title2):
    song_titles_parser = SongTitlesParser(SongTitlesSplitter())

    parsed = song_titles_parser.parse(f"{prefix}{text1}{connector}{text2}")

    assert parsed.song_title1 == SongTitle(artist1, title1)
    assert parsed.song_title2 == SongTitle(artist2, title2)


def test_parsed_song_titles(song_title1, song_title2):
    split_text = [song_title1.__str__(), song_title2.__str__()]

    parser = FullTitlesParser()
    parsed = parser.parse_song_titles(split_text)

    assert parsed.song_title1 == song_title1
    assert parsed.song_title2 == song_title2


def test_parsed_artists_only():
    parser = ArtistsParser()
    parsed = parser.parse_song_titles(['Led Zeppelin', 'Steppenwolf'])

    assert parsed.song_title1 == ArtistTitle('Led Zeppelin')
    assert parsed.song_title2 == ArtistTitle('Steppenwolf')


def test_artist_only_str():
    assert str(ArtistTitle('Led Zeppelin')) == 'Led Zeppelin'

