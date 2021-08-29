import pytest
from songs.model import Lyrics, Paragraphs, Paragraph, Line


two_paragraphs_text = 'First paragraph\n\nSecond paragraph'


def test_lyrics_text():
    assert Lyrics(two_paragraphs_text).text == two_paragraphs_text


def test_get_paragraphs_from_lyrics():
    assert Lyrics(two_paragraphs_text).paragraphs == Paragraphs.from_text(two_paragraphs_text)


def test_lyrics_to_string():
    assert str(Lyrics(two_paragraphs_text)) == two_paragraphs_text


def test_paragraph():
    line1 = Line('line 1')
    line2 = Line('line 2')
    paragraph = Paragraph([line1, line2])

    assert paragraph.text == 'line 1\nline 2\n\n'


def test_paragraphs():
    text = 'line 1\nline 2\n\nline 3\nline 4\n\n'
    paragraphs = Paragraphs.from_text(text)

    assert paragraphs[0] == Paragraph([Line('line 1'), Line('line 2')])
    assert paragraphs[1] == Paragraph([Line('line 3'), Line('line 4')])


def test_paragraphs_from_text_without_ending_new_lines():
    text = 'line 1\nline 2\n\nline 3\nline 4'

    paragraphs = Paragraphs.from_text(text)

    assert paragraphs[0] == Paragraph([Line('line 1'), Line('line 2')])
    assert paragraphs[1] == Paragraph([Line('line 3'), Line('line 4')])
