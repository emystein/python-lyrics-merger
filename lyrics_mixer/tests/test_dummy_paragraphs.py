from lyrics_mixer.tests.dummy_paragraphs import DummyChapter
from songs.model import Paragraphs, Paragraph


def test_zero_paragraphs():
    paragraphs = DummyChapter.number(1).paragraph_count(0).lines_per_paragraph(1)

    assert paragraphs == []


def test_zero_lines():
    paragraphs = DummyChapter.number(1).paragraph_count(1).lines_per_paragraph(0)

    assert paragraphs == [Paragraph([])]


def test_two_paragraphs_with_two_lines_each():
    paragraphs = DummyChapter.number(1).paragraph_count(2).lines_per_paragraph(2)

    expected_paragraphs = Paragraphs.from_text('chapter 1, paragraph 1, line 1\nchapter 1, paragraph 1, line 2\n\nchapter 1, paragraph 2, line 1\nchapter 1, paragraph 2, line 2\n')

    assert paragraphs == expected_paragraphs

