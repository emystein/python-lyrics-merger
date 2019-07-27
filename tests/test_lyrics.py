import pytest
from app.lyrics import Lyrics


def test_lyrics_text():
    lyrics = Lyrics('First paragraph\n\nSecond paragraph')
    assert lyrics.text == 'First paragraph\n\nSecond paragraph'


def test_get_paragraphs_from_lyrics():
    lyrics = Lyrics('First paragraph\n\nSecond paragraph')
    assert lyrics.paragraphs() == ['First paragraph', 'Second paragraph']


def test_lyrics_to_string():
    lyrics = Lyrics('First paragraph\n\nSecond paragraph')
    to_string = str(lyrics)
    assert to_string == 'First paragraph\n\nSecond paragraph'
