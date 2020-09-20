import pytest

from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser


@pytest.mark.parametrize('prefix', ['', '@lyricsmixer mezclá '])
@pytest.mark.parametrize('connector', [', ', ' y ', ' and '])
@pytest.mark.parametrize(
    'text1, text2, artist1, title1, artist2, title2',
    [
        ('Led Zeppelin - Stairway to Heaven', 'Steppenwolf - Born to be wild',
         'Led Zeppelin', 'Stairway to Heaven', 'Steppenwolf', 'Born to be wild'),
        ('Led Zeppelin', 'Steppenwolf', 'Led Zeppelin', '', 'Steppenwolf', '')
    ]
)
def test_parse_song_titles(prefix, connector, text1, text2, artist1, title1, artist2, title2):
    song_titles_parser = SongTitlesParser(SongTitlesSplitter())

    parsed = song_titles_parser.parse(f"{prefix}{text1}{connector}{text2}")

    assert parsed.artist1 == artist1
    assert parsed.title1 == title1
    assert parsed.artist2 == artist2
    assert parsed.title2 == title2
