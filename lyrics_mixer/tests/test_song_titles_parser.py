import pytest
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser, ParsedSongTitles, ParsedArtists
from songs.model import SongTitle
from songs.tests.fixtures.song_titles import song_title1, song_title2
from lyrics_mixer.tests.fixtures.mixer import mixer

@pytest.mark.parametrize('prefix', ['', '@lyricsmixer mezcla '])
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

    assert parsed.song_title1 == SongTitle(artist1, title1)
    assert parsed.song_title2 == SongTitle(artist2, title2)


def test_parsed_song_titles(song_title1, song_title2):
    split_text = [song_title1.__str__(), song_title2.__str__()]

    parsed = ParsedSongTitles(split_text)

    assert parsed.song_title1 == song_title1
    assert parsed.song_title2 == song_title2


def test_parsed_artists_only():
    split_text = ['Led Zeppelin', 'Steppenwolf']

    parsed = ParsedArtists(split_text)

    assert parsed.song_title1 == SongTitle.artist_only('Led Zeppelin')
    assert parsed.song_title2 == SongTitle.artist_only('Steppenwolf')


def test_mix_titles(mixer):
    parsed = ParsedSongTitles(['U2 - One', 'The Police - Roxanne'])

    mixed_lyrics = parsed.mix_using(mixer)

    assert mixed_lyrics.has_content()


def test_mix_artists(mixer):
    parsed = ParsedArtists(['U2', 'The Police'])

    mixed_lyrics = parsed.mix_using(mixer)

    assert mixed_lyrics.has_content()
