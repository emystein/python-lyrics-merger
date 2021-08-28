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
    text = 'line 1\nline 2\n\nline 3\nline 4\nline 5\n\nline 6\n\n'
    paragraphs = Paragraphs.from_text(text)

    assert paragraphs.size == 3
    assert paragraphs[0] == Paragraph([Line('line 1'), Line('line 2')])
    assert paragraphs[1] == Paragraph([Line('line 3'), Line('line 4'), Line('line 5')])
    assert paragraphs[2] == Paragraph([Line('line 6')])
    assert paragraphs.text == text


def test_zip_paragraphs():
    paragraphs1 = Paragraphs.from_text('paragraph 1 line 1\nparagraph 1 line 2\n\nparagraph 1 line 3\nparagraph 1 line 4')
    paragraphs2 = Paragraphs.from_text('paragraph 2 line 1\nparagraph 2 line 2\n\nparagraph 2 line 3\nparagraph 2 line 4')

    all_paragraphs = [paragraphs1, paragraphs2]

    assert list(zip(*all_paragraphs)) == [
        (Paragraph([Line('paragraph 1 line 1'), Line('paragraph 1 line 2')]),
         Paragraph([Line('paragraph 2 line 1'), Line('paragraph 2 line 2')])),

        (Paragraph([Line('paragraph 1 line 3'), Line('paragraph 1 line 4')]),
         Paragraph([Line('paragraph 2 line 3'), Line('paragraph 2 line 4')])),
    ]


def test_paragraphs_from_list():
    line1 = Line('line 1')
    line2 = Line('line 2')
    paragraph1 = Paragraph([line1, line2])
    line3 = Line('line 3')
    line4 = Line('line 4')
    paragraph2 = Paragraph([line3, line4])

    paragraphs = Paragraphs.from_list([paragraph1, paragraph2])

    assert paragraphs.text == 'line 1\nline 2\n\nline 3\nline 4\n\n'


