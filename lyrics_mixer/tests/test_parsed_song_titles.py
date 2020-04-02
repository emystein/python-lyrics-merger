import pytest
from songs.model import SongTitle, EmptySongTitle, ArtistOnlySongTitle
from lyrics_mixer.mix_commands import ParsedSongTitles, ParsedArtists, SongTitlesMixCommand, ArtistsMixCommand
from songs.tests.fixtures.song_titles import song_title1, song_title2


@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_parse_song_titles(song_title1, song_title2):
    split_text = [song_title1.__str__(), song_title2.__str__()]

    parsed = ParsedSongTitles(split_text)

    assert parsed.song_title1 == song_title1
    assert parsed.song_title2 == song_title2
    assert isinstance(parsed.mix_command(), SongTitlesMixCommand)


def test_parse_artists_only():
    split_text = ['Led Zeppelin', 'Steppenwolf']

    parsed = ParsedArtists(split_text)

    assert parsed.song_title1 == ArtistOnlySongTitle('Led Zeppelin')
    assert parsed.song_title2 == ArtistOnlySongTitle('Steppenwolf')
    assert isinstance(parsed.mix_command(), ArtistsMixCommand)
