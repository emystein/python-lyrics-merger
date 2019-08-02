import pytest
from lyrics_merger.lyrics import Lyrics


def test_lyrics_text():
    lyrics = Lyrics('First paragraph\n\nSecond paragraph')
    assert lyrics.text == 'First paragraph\n\nSecond paragraph'


def test_get_paragraphs_from_lyrics():
    lyrics = Lyrics('First paragraph\n\nSecond paragraph')
    assert lyrics.paragraphs() == ['First paragraph', 'Second paragraph']


def test_lyrics_to_string():
    lyrics = Lyrics('First paragraph\n\nSecond paragraph')
    assert str(lyrics) == 'First paragraph\n\nSecond paragraph'
