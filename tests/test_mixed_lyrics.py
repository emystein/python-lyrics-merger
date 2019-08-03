import pytest
from lyrics_mixer.lyrics_mixer import ParagraphInterleaveLyricsEditor, MixedLyrics
import tests.song_factory

def test_mixed_lyrics():
	song1 = tests.song_factory.create_song_stairway_to_heaven()
	song2 = tests.song_factory.create_song_born_to_be_wild()
	lyrics_editor = ParagraphInterleaveLyricsEditor()
	expected = lyrics_editor.interleave_lyrics(song1, song2)

	mixed_lyrics = MixedLyrics(song1, song2, [], expected.paragraphs)

	assert mixed_lyrics.title == str(song1.title) + ', ' + str(song2.title)
	assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)
