import pytest
from songs.model import Lyrics


two_paragraphs_text = 'First paragraph\n\nSecond paragraph'


def test_lyrics_text():
    assert Lyrics(two_paragraphs_text).text == two_paragraphs_text


def test_get_lines_from_lyrics():
    lyrics = Lyrics('First line\nSecond line\n\nThird line')
    assert lyrics.lines() == ['First line', 'Second line', '', 'Third line']


def test_get_paragraphs_from_lyrics():
    assert Lyrics(two_paragraphs_text).paragraphs() == ['First paragraph', 'Second paragraph']


def test_lyrics_to_string():
    assert str(Lyrics(two_paragraphs_text)) == two_paragraphs_text
