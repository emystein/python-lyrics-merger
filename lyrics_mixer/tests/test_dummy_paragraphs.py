from lyrics_mixer.tests.dummy_paragraphs import DummyParagraphs
from songs.model import Paragraphs, Paragraph


def test_zero_paragraphs():
    paragraphs = DummyParagraphs.for_lyrics(1).with_paragraphs(0).each_with_lines(1)

    assert paragraphs == []


def test_zero_lines():
    paragraphs = DummyParagraphs.for_lyrics(1).with_paragraphs(1).each_with_lines(0)

    assert paragraphs == [Paragraph([])]


def test_two_paragraphs_with_two_lines_each():
    paragraphs = DummyParagraphs.for_lyrics(1).with_paragraphs(2).each_with_lines(2)

    expected_paragraphs = Paragraphs.from_text('lyrics 1, paragraph 1, line 1\nlyrics 1, paragraph 1, line 2\n\nlyrics 1, paragraph 2, line 1\nlyrics 1, paragraph 2, line 2\n')

    assert paragraphs == expected_paragraphs

