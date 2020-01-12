import pytest
from lyrics_mixer.mix_commands import ArtistsMixCommand, SongTitlesMixCommand
from songs.tests.fixtures.song_titles import song_title1, song_title2
from unittest.mock import Mock


def test_artist_mix_command():
    artists = ['Led Zeppelin', 'Steppenwolf']

    mix_command = ArtistsMixCommand(artists)

    assert mix_command.song_titles == []
    assert mix_command.artists == artists
    assert mix_command.artist1 == artists[0]
    assert mix_command.artist2 == artists[1]

    lyrics_mixer = Mock()

    mix_command.mix(lyrics_mixer)

    lyrics_mixer.mix_random_lyrics_by_artists.assert_called_with(
        'Led Zeppelin', 'Steppenwolf')


def test_artist_mix_command_accepts_text():
    artists = ['Led Zeppelin', 'Steppenwolf']

    mix_command = ArtistsMixCommand(artists)

    assert mix_command.accepts('Led Zeppelin and Steppenwolf')


@pytest.mark.usefixtures('song_title1', 'song_title2')
def test_song_titles_mix_command(song_title1, song_title2):
    flat_titles = [
        f"{title.artist}-{title.title}" for title in [song_title1, song_title2]]

    mix_command = SongTitlesMixCommand(flat_titles)

    assert mix_command.song_titles == [song_title1, song_title2] 

    lyrics_mixer = Mock()

    mix_command.mix(lyrics_mixer)

    lyrics_mixer.mix_two_specific_lyrics.assert_called_with(
        song_title1, song_title2)


def test_song_titles_mix_command_accepts_text():
    titles = ['Led Zeppelin - Stairway to Heaven', 'Steppenwolf - Born to be wild']

    mix_command = SongTitlesMixCommand(titles)

    flat_titles = 'Led Zeppelin - Stairway to Heaven, Steppenwolf - Born to be wild'

    assert mix_command.accepts(flat_titles)
