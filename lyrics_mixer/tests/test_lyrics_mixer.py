import pytest
from unittest.mock import Mock
from lyrics_mixer.tests.fixtures.mocks import lyrics_library_mock
import songs.tests.song_factory
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.song_titles_parser import ParsedArtists
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMixStrategy, ParagraphInterleaveLyricsMixStrategy, MixedLyrics, EmptyMixedLyrics


lyrics_mix_strategy = LineInterleaveLyricsMixStrategy()


def test_two_random_songs_mixer(lyrics_library_mock, song1, song2):
    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

    lyrics_library_mock.get_random_songs.return_value = [song1, song2]

    mixed_lyrics = mixer.mix_two_random_lyrics()

    assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_two_random_songs_by_artists_mixer(lyrics_library_mock, song1, song2):
    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

    lyrics_library_mock.get_random_songs_by_artists.return_value = [song1, song2]

    mixed_lyrics = mixer.mix_random_lyrics_by_artists(song1.artist, song2.artist)

    assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_two_specific_songs_mixer(lyrics_library_mock, song1, song2):
    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

    lyrics_library_mock.get_songs.return_value = [song1, song2]

    mixed_lyrics = mixer.mix_two_specific_lyrics(song1.title, song2.title)

    assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_mix_parsed_song_titles(lyrics_library_mock, song1, song2):
    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

    lyrics_library_mock.get_random_songs_by_artists.return_value = [
        song1, song2]

    parsed_song_titles = ParsedArtists(['Led Zeppelin', 'Steppenwolf'])

    mixed_lyrics = mixer.mix_parsed_song_titles(parsed_song_titles)

    assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_exception_on_mix_lyrics(lyrics_library_mock):
    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

    lyrics_picker = Mock()

    lyrics_picker.pick_two.side_effect = RuntimeError('Download error')

    mixed_lyrics = mixer.mix_lyrics(lyrics_picker)

    assert mixed_lyrics == EmptyMixedLyrics()


def test_mixed_lyrics(song1, song2):
    lyrics_editor = ParagraphInterleaveLyricsMixStrategy()
    expected = lyrics_editor.mix(song1, song2)

    mixed_lyrics = MixedLyrics(song1, song2, [], expected.paragraphs)

    assert mixed_lyrics.title == str(song1.full_title()) + ', ' + str(song2.full_title())
    assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)
