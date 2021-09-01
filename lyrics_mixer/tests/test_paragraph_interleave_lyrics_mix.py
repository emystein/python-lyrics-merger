from lyrics_mixer.lyrics_mix_strategies import ParagraphInterleaveLyricsMix
from lyrics_mixer.tests.dummy_paragraphs import DummyChapter
from songs.model import SongTitle, Lyrics, Paragraphs, Line, Paragraph

song_title1 = SongTitle('artist1', 'title1')
song_title2 = SongTitle('artist2', 'title2')

lyrics_mix_strategy = ParagraphInterleaveLyricsMix()

line_1_1 = Line('line 1 1')
line_1_2 = Line('line 1 2')
line_1_3 = Line('line 1 3')
line_2_1 = Line('line 2 1')
line_2_2 = Line('line 2 2')
line_2_3 = Line('line 2 3')

paragraph_1_1 = Paragraph([line_1_1])
paragraph_1_2 = Paragraph([line_1_2])
paragraph_2_1 = Paragraph([line_2_1])
paragraph_2_2 = Paragraph([line_2_2])


def test_mix_with_same_number_of_paragraphs():
    paragraphs1 = DummyChapter.number(1).paragraph_count(2).lines_per_paragraph(1)
    lyrics1 = Lyrics(song_title1, paragraphs1)

    paragraphs2 = DummyChapter.number(2).paragraph_count(2).lines_per_paragraph(1)
    lyrics2 = Lyrics(song_title2, paragraphs2)

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    expected_paragraphs = Paragraphs.from_text('chapter 1, paragraph 1, line 1\n\nchapter 2, paragraph 1, line 1\n\nchapter 1, paragraph 2, line 1\n\nchapter 2, paragraph 2, line 1\n\n')

    assert mixed_lyrics.paragraphs == expected_paragraphs


def test_mix_with_first_lyrics_with_2_paragraphs_and_second_lyrics_with_1_paragraph():
    lyrics1 = Lyrics(song_title1, [paragraph_1_1, paragraph_1_2])
    lyrics2 = Lyrics(song_title2, [paragraph_2_1])

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    assert mixed_lyrics.paragraphs == [paragraph_1_1, paragraph_2_1]


def test_mix_with_first_lyrics_with_1_paragraph_and_second_lyrics_with_2_paragraphs():
    lyrics1 = Lyrics(song_title1, [paragraph_1_1])
    lyrics2 = Lyrics(song_title2, [paragraph_2_1, paragraph_2_2])

    mixed_lyrics = lyrics_mix_strategy.mix(lyrics1, lyrics2)

    assert mixed_lyrics.paragraphs == [paragraph_1_1, paragraph_2_1]
