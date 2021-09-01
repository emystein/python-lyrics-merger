import pytest
from lyrics_mixer.lyrics_mix_strategies import flatten, LineInterleaveLyricsMix
from songs.model import SongTitle, Lyrics, Paragraphs, Paragraph
from lyrics_mixer.tests.dummy_paragraphs import DummyParagraphs

song_title1 = SongTitle('artist1', 'title1')
song_title2 = SongTitle('artist2', 'title2')

lyrics_mix_strategy = LineInterleaveLyricsMix()


def test_mix_with_same_number_of_lines():
    paragraphs1 = DummyParagraphs.chapter(1).count(1).lines_per_each(2)
    lyrics1 = Lyrics(song_title1, paragraphs1)

    paragraphs2 = DummyParagraphs.chapter(2).count(1).lines_per_each(2)
    lyrics2 = Lyrics(song_title2, paragraphs2)

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    expected_lines = flatten([flatten(zip(p1.lines, p2.lines)) for p1, p2 in zip(paragraphs1, paragraphs2)])

    assert mixed_lyrics.paragraphs == [Paragraph(expected_lines)]


def test_mix_with_first_lyrics_with_2_lines_and_second_lyrics_with_1_line():
    lyrics1 = Lyrics.with_text('lyrics 1 line 1\nlyrics 1 line 2')
    lyrics2 = Lyrics.with_text('lyrics 2 line 1')

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    expected_paragraphs = Paragraphs.from_text('lyrics 1 line 1\nlyrics 2 line 1')

    assert mixed_lyrics.paragraphs == expected_paragraphs


def test_mix_with_first_lyrics_with_1_line_and_second_lyrics_with_2_lines():
    lyrics1 = Lyrics.with_text('lyrics 1 line 1')
    lyrics2 = Lyrics.with_text('lyrics 2 line 1\nlyrics 2 line 2')

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    expected_paragraphs = Paragraphs.from_text('lyrics 1 line 1\nlyrics 2 line 1')

    assert mixed_lyrics.paragraphs == expected_paragraphs


def test_mix_with_first_paragraph_containing_two_lines_and_second_paragraph_containing_one_line():
    lyrics1 = Lyrics.with_text('lyrics 1 line 1\nlyrics 1 line 2\n\nlyrics 1 line 3')
    lyrics2 = Lyrics.with_text('lyrics 2 line 1\nlyrics 2 line 2\n\nlyrics 2 line 3')

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    expected_paragraphs = Paragraphs.from_text(
        'lyrics 1 line 1\nlyrics 2 line 1\nlyrics 1 line 2\nlyrics 2 line 2\nlyrics 1 line 3\nlyrics 2 line 3\n\n')

    assert mixed_lyrics.paragraphs == expected_paragraphs


def test_mix_with_first_paragraph_containing_one_line_and_second_paragraph_containing_two_lines():
    lyrics1 = Lyrics.with_text('lyrics 1 line 1\n\nlyrics 1 line 2\nlyrics 1 line 3')
    lyrics2 = Lyrics.with_text('lyrics 2 line 1\n\nlyrics 2 line 2\nlyrics 2 line 3')

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    expected_paragraphs = Paragraphs.from_text(
        'lyrics 1 line 1\nlyrics 2 line 1\nlyrics 1 line 2\nlyrics 2 line 2\nlyrics 1 line 3\nlyrics 2 line 3\n\n')

    assert mixed_lyrics.paragraphs == expected_paragraphs
