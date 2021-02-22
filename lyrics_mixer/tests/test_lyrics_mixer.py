import pytest
from unittest.mock import Mock

from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, MixedLyrics
from lyrics_mixer.tests.fixtures.mixer import lyrics_mix

def test_mix_two_random_lyrics(lyrics_mix, song1, song2):
    lyrics_library = Mock()

    mixer = LyricsMixer(lyrics_library, lyrics_mix)

    lyrics_library.get_random_songs.return_value = [song1, song2]

    assert mixer.mix_two_random_lyrics() == lyrics_mix.mix(song1, song2)


def test_mix_random_lyrics_by_artists(lyrics_mix, song1, song2):
    lyrics_library = Mock()

    mixer = LyricsMixer(lyrics_library, lyrics_mix)

    lyrics_library.get_random_songs_by_artists.return_value = [song1, song2]

    assert mixer.mix_random_lyrics_by_artists(song1.artist, song2.artist) == lyrics_mix.mix(song1, song2)


def test_mix_two_specific_lyrics(lyrics_mix, song1, song2):
    lyrics_library = Mock()

    mixer = LyricsMixer(lyrics_library, lyrics_mix)

    lyrics_library.get_song.side_effect = [song1, song2]

    assert mixer.mix_two_specific_lyrics(song1.artist, song1.title, song2.artist, song2.title) == lyrics_mix.mix(song1,
                                                                                                                 song2)

def test_exception_on_mix_lyrics(lyrics_mix):
    lyrics_library = Mock()

    mixer = LyricsMixer(lyrics_library, lyrics_mix)

    lyrics_picker_mock = Mock()

    lyrics_picker_mock.pick_two.side_effect = RuntimeError('Download error')

    assert mixer.mix_lyrics(lyrics_picker_mock) == MixedLyrics.empty()


def test_mixed_lyrics(lyrics_mix, song1, song2):
    expected = lyrics_mix.mix(song1, song2)

    mixed_lyrics = MixedLyrics(song1, song2, [], expected.paragraphs)

    assert mixed_lyrics.title == f"{song1.artist} - {song1.title}, {song2.artist} - {song2.title}"
    assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)

