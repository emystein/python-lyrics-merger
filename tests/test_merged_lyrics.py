import pytest
from app.lyrics_merge import LyricsEditor
from app.lyrics_merge import MergedLyrics
import tests.song_factory

def test_merged_lyrics():
	song1 = tests.song_factory.create_song1()
	song2 = tests.song_factory.create_song2()
	lyrics_editor = LyricsEditor()
	expected = lyrics_editor.interleave_lyrics(song1, song2)

	merged_lyrics = MergedLyrics(song1, song2, expected.paragraphs)

	assert merged_lyrics.title == str(song1.title) + ', ' + str(song2.title)
	assert merged_lyrics.text == '\n\n'.join(expected.paragraphs)
