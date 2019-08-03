import pytest
from lyrics_merger.lyrics_merge import InterleaveParagraphsLyricsEditor, MergedLyrics
import tests.song_factory

def test_merged_lyrics():
	song1 = tests.song_factory.create_song_stairway_to_heaven()
	song2 = tests.song_factory.create_song_born_to_be_wild()
	lyrics_editor = InterleaveParagraphsLyricsEditor()
	expected = lyrics_editor.interleave_lyrics(song1, song2)

	merged_lyrics = MergedLyrics(song1, song2, expected.paragraphs)

	assert merged_lyrics.title == str(song1.title) + ', ' + str(song2.title)
	assert merged_lyrics.text == '\n\n'.join(expected.paragraphs)
