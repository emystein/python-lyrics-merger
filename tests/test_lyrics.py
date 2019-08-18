import pytest
from songs.model import Lyrics


def test_lyrics_text():
    lyrics = Lyrics('First paragraph\n\nSecond paragraph')
    assert lyrics.text == 'First paragraph\n\nSecond paragraph'


def test_get_lines_from_lyrics():
    lyrics = Lyrics('First line\nSecond line\n\nThird line')
    assert lyrics.lines() == ['First line', 'Second line', '', 'Third line']


def test_get_paragraphs_from_lyrics():
    lyrics = Lyrics('First paragraph\n\nSecond paragraph')
    assert lyrics.paragraphs() == ['First paragraph', 'Second paragraph']


def test_lyrics_to_string():
    lyrics = Lyrics('First paragraph\n\nSecond paragraph')
    assert str(lyrics) == 'First paragraph\n\nSecond paragraph'
