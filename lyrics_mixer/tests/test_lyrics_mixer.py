import pytest
from unittest.mock import Mock

from songs.model import SongTitle
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.lyrics_mixer import MixedLyrics
from lyrics_mixer.tests.fixtures.mixer import lyrics_mixer, lyrics_mix


def test_exception_on_mix_lyrics(lyrics_mixer):
    mock_lyrics_picker = Mock()

    mock_lyrics_picker.pick.side_effect = RuntimeError('Download error')

    assert lyrics_mixer.mix_lyrics(mock_lyrics_picker) == MixedLyrics.empty()


def test_mixed_lyrics(lyrics_mix, song1, song2):
    expected = lyrics_mix.mix(song1, song2)

    mixed_lyrics = MixedLyrics([song1, song2], [], expected.paragraphs)

    assert mixed_lyrics.title == f"{song1.title}, {song2.title}"
    assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)
