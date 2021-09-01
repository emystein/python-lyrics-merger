from lyrics_mixer.lists import flatten
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix
from songs.model import SongTitle, Lyrics, Paragraph, Line
from lyrics_mixer.tests.dummy_paragraphs import DummyChapter

song_title1 = SongTitle('artist1', 'title1')
song_title2 = SongTitle('artist2', 'title2')

line_1_1 = Line('lyrics 1 line 1')
line_1_2 = Line('lyrics 1 line 2')
line_1_3 = Line('lyrics 1 line 3')
line_2_1 = Line('lyrics 2 line 1')
line_2_2 = Line('lyrics 2 line 2')
line_2_3 = Line('lyrics 2 line 3')

lyrics_mix_strategy = LineInterleaveLyricsMix()


def test_mix_with_same_number_of_lines():
    paragraphs1 = DummyChapter.number(1).paragraph_count(1).lines_per_paragraph(2)
    lyrics1 = Lyrics(song_title1, paragraphs1)

    paragraphs2 = DummyChapter.number(2).paragraph_count(1).lines_per_paragraph(2)
    lyrics2 = Lyrics(song_title2, paragraphs2)

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    expected_lines = [
        paragraphs1[0].lines[0], paragraphs2[0].lines[0],
        paragraphs1[0].lines[1], paragraphs2[0].lines[1]
    ]

    assert mixed_lyrics.paragraphs == [Paragraph(expected_lines)]


def test_mix_with_first_lyrics_with_2_lines_and_second_lyrics_with_1_line():
    lyrics1 = Lyrics(song_title1, [Paragraph([line_1_1, line_1_2])])
    lyrics2 = Lyrics(song_title2, [Paragraph([line_2_1])])

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    assert mixed_lyrics.paragraphs == [Paragraph([line_1_1, line_2_1])]


def test_mix_with_first_lyrics_with_1_line_and_second_lyrics_with_2_lines():
    lyrics1 = Lyrics(song_title1, [Paragraph([line_1_1])])
    lyrics2 = Lyrics(song_title2, [Paragraph([line_2_1, line_2_1])])

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    assert mixed_lyrics.paragraphs == [Paragraph([line_1_1, line_2_1])]


def test_mix_with_first_paragraph_containing_two_lines_and_second_paragraph_containing_one_line():
    lyrics1 = Lyrics(song_title1, [Paragraph([line_1_1, line_1_2]), Paragraph([line_1_3])])
    lyrics2 = Lyrics(song_title2, [Paragraph([line_2_1, line_2_2]), Paragraph([line_2_3])])

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    assert mixed_lyrics.paragraphs == [Paragraph([line_1_1, line_2_1, line_1_2, line_2_2, line_1_3, line_2_3])]


def test_mix_with_first_paragraph_containing_one_line_and_second_paragraph_containing_two_lines():
    lyrics1 = Lyrics(song_title1, [Paragraph([line_1_1]), Paragraph([line_1_2, line_1_3])])
    lyrics2 = Lyrics(song_title2, [Paragraph([line_2_1]), Paragraph([line_2_2, line_2_3])])

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    assert mixed_lyrics.paragraphs == [Paragraph([line_1_1, line_2_1, line_1_2, line_2_2, line_1_3, line_2_3])]
