import pytest
from app.lyrics_editor import LyricsEditor

def test_split_lyrics_paragraphs():
	file = open('tests/led_zeppelin_-_stairway_to_heaven.txt', 'r') 
	lyrics = file.read() 
	lyrics_editor = LyricsEditor()
	paragraphs = lyrics_editor.split_paragraphs(lyrics)
	assert len(paragraphs) == 12

def test_merge_lyrics_with_same_number_of_paragraphs():
	lyrics1 = 'lyrics 1 first paragraph\n\nlyrics 1 second paragraph'
	lyrics2 = 'lyrics 2 first paragraph\n\nlyrics 2 second paragraph'
	lyrics_editor = LyricsEditor()
	merged_lyrics = lyrics_editor.merge_lyrics(lyrics1, lyrics2)
	assert merged_lyrics == ['lyrics 1 first paragraph', 'lyrics 2 first paragraph', 'lyrics 1 second paragraph', 'lyrics 2 second paragraph'] 

def test_merge_lyrics_with_first_lyrics_with_2_paragraphs_and_second_lyrics_with_1_paragraph():
	lyrics1 = 'lyrics 1 first paragraph\n\nlyrics 1 second paragraph'
	lyrics2 = 'lyrics 2 first paragraph'
	lyrics_editor = LyricsEditor()
	merged_lyrics = lyrics_editor.merge_lyrics(lyrics1, lyrics2)
	assert merged_lyrics == ['lyrics 1 first paragraph', 'lyrics 2 first paragraph']

def test_merge_lyrics_with_first_lyrics_with_1_paragraph_and_second_lyrics_with_2_paragraphs():
	lyrics1 = 'lyrics 1 first paragraph'
	lyrics2 = 'lyrics 2 first paragraph\n\nlyrics 2 second paragraph'
	lyrics_editor = LyricsEditor()
	merged_lyrics = lyrics_editor.merge_lyrics(lyrics1, lyrics2)
	assert merged_lyrics == ['lyrics 1 first paragraph', 'lyrics 2 first paragraph']