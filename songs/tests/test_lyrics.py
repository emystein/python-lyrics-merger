import pytest
from songs.model import Lyrics, Paragraphs, Paragraph, Line


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


def test_paragraphs():
    paragraphs = Paragraphs('line 1\nline 2\n\nline 3\nline 4\nline 5\n\nline 6')

    assert paragraphs[0] == Paragraph([Line('line 1'), Line('line 2')])
    assert paragraphs[1] == Paragraph([Line('line 3'), Line('line 4'), Line('line 5')])
    assert paragraphs[2] == Paragraph([Line('line 6')])
