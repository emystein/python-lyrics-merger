import pytest
from lyrics_mixer.lyrics_mixer import MixedLyrics
from lyrics_mixer.lyrics_mix_strategies import ParagraphInterleaveLyricsMix
import songs.tests.song_factory
from songs.tests.fixtures.songs import song1, song2


def test_mixed_lyrics(song1, song2):
	lyrics_editor = ParagraphInterleaveLyricsMix()
	expected = lyrics_editor.mix(song1, song2)

	mixed_lyrics = MixedLyrics(song1, song2, [], expected.paragraphs)

	assert mixed_lyrics.title == str(song1.title) + ', ' + str(song2.title)
	assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)
