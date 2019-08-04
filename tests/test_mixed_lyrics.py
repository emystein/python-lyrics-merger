import pytest
from lyrics_mixer.lyrics_mixer import ParagraphInterleaveLyricsMix, MixedLyrics
import tests.song_factory

@pytest.fixture
def song1():
	return tests.song_factory.create_song_stairway_to_heaven()


@pytest.fixture
def song2():
	return tests.song_factory.create_song_born_to_be_wild()


def test_mixed_lyrics(song1, song2):
	lyrics_editor = ParagraphInterleaveLyricsMix()
	expected = lyrics_editor.mix_lyrics(song1, song2)

	mixed_lyrics = MixedLyrics(song1, song2, [], expected.paragraphs)

	assert mixed_lyrics.title == str(song1.title) + ', ' + str(song2.title)
	assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)
