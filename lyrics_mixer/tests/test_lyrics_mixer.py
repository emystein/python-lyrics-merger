import pytest
from unittest.mock import Mock

from lyrics_mixer.lyrics_data_source import LyricsDataSource
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, MixedLyrics

lyrics_mix = LineInterleaveLyricsMix()


def test_mix_two_random_lyrics(song1, song2):
    lyrics_library_mock = Mock()

    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix)

    lyrics_library_mock.get_random_songs.return_value = [song1, song2]

    assert mixer.mix_two_random_lyrics() == lyrics_mix.mix(song1, song2)


def test_mix_random_lyrics_by_artists(song1, song2):
    lyrics_library_mock = Mock()

    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix)

    lyrics_library_mock.get_random_songs_by_artists.return_value = [song1, song2]

    assert mixer.mix_random_lyrics_by_artists(song1.artist, song2.artist) == lyrics_mix.mix(song1, song2)


@pytest.mark.slow_integration_test
def test_mix_random_lyrics_by_artists_integration():
    mixer = LyricsMixer(LyricsDataSource(), lyrics_mix)

    mixed_lyrics = mixer.mix_random_lyrics_by_artists('Led Zeppelin', 'Steppenwolf')

    assert mixed_lyrics.has_content()


def test_mix_two_specific_lyrics(song1, song2):
    lyrics_library_mock = Mock()

    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix)

    lyrics_library_mock.get_song.side_effect = [song1, song2]

    assert mixer.mix_two_specific_lyrics(song1.artist, song1.title, song2.artist, song2.title) == lyrics_mix.mix(song1,
                                                                                                                 song2)


@pytest.mark.slow_integration_test
def test_mix_two_specific_lyrics_integration():
    mixer = LyricsMixer(LyricsDataSource(), lyrics_mix)

    mixed_lyrics = mixer.mix_two_specific_lyrics('Led Zeppelin', 'Stairway to Heaven', 'Steppenwolf', 'Born to be wild')

    assert mixed_lyrics.has_content()


def test_exception_on_mix_lyrics():
    lyrics_library_mock = Mock()

    mixer = LyricsMixer(lyrics_library_mock, lyrics_mix)

    lyrics_picker_mock = Mock()

    lyrics_picker_mock.pick_two.side_effect = RuntimeError('Download error')

    assert mixer.mix_lyrics(lyrics_picker_mock) == MixedLyrics.empty()


def test_mixed_lyrics(song1, song2):
    expected = lyrics_mix.mix(song1, song2)

    mixed_lyrics = MixedLyrics(song1, song2, [], expected.paragraphs)

    assert mixed_lyrics.title == f"{song1.artist} - {song1.title}, {song2.artist} - {song2.title}"
    assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)

