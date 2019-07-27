import pytest
from app.lyrics_editor import LyricsEditor

def test_split_lyrics_paragraphs():
	file = open('tests/led_zeppelin_-_stairway_to_heaven.txt', 'r') 
	lyrics = file.read() 
	lyrics_editor = LyricsEditor()
	paragraphs = lyrics_editor.split_paragraphs(lyrics)
	assert len(paragraphs) == 12