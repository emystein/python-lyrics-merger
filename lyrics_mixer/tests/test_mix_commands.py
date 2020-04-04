import pytest
from lyrics_mixer.song_titles_parser import ParsedSongTitles, ParsedArtists
from lyrics_mixer.lyrics_mixer import ArtistsMixCommand, SongTitlesMixCommand, MixCommands
from songs.tests.fixtures.song_titles import song_title1, song_title2
from unittest.mock import Mock


def test_artist_mix_command_accepts_text():
    split_text = ['Led Zeppelin', 'Steppenwolf']

    parsed = ParsedArtists(split_text)

    mix_command = ArtistsMixCommand()

    assert mix_command.accepts(parsed)


def test_artist_mix_command():
    split_text = ['Led Zeppelin', 'Steppenwolf']

    parsed = ParsedArtists(split_text)

    mix_command = ArtistsMixCommand()

    lyrics_mixer = Mock()

    mix_command.mix(parsed, lyrics_mixer)

    lyrics_mixer.mix_random_lyrics_by_artists.assert_called_with(
        'Led Zeppelin', 'Steppenwolf')


@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_song_titles_mix_command_accepts_text(song_title1, song_title2):
    split_text = [song_title1.__str__(), song_title2.__str__()]

    parsed = ParsedSongTitles(split_text)

    mix_command = SongTitlesMixCommand()

    assert mix_command.accepts(parsed)


@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_song_titles_mix_command(song_title1, song_title2):
    split_text = [song_title1.__str__(), song_title2.__str__()]

    parsed = ParsedSongTitles(split_text)

    mix_command = SongTitlesMixCommand()

    lyrics_mixer = Mock()

    mix_command.mix(parsed, lyrics_mixer)

    lyrics_mixer.mix_two_specific_lyrics.assert_called_with(
        song_title1, song_title2)


def test_select_song_titles_mix_command():
    parsed = ParsedSongTitles([song_title1.__str__(), song_title2.__str__()])

    mix_command = MixCommands.select_for(parsed)

    assert isinstance(mix_command, SongTitlesMixCommand)


def test_select_artist_mix_command():
    parsed = ParsedArtists(['Led Zeppelin', 'Steppenwolf'])

    mix_command = MixCommands.select_for(parsed)

    assert isinstance(mix_command, ArtistsMixCommand)
