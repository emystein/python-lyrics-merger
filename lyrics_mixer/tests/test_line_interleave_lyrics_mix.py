import pytest
from lyrics_mixer.lyrics_mixer import LineInterleaveLyricsMix
from songs.model import SongTitle, Lyrics, Paragraphs

song_title1 = SongTitle('artist1', 'title1')
song_title2 = SongTitle('artist2', 'title2')


@pytest.fixture
def lyrics_editor():
    return LineInterleaveLyricsMix()


def test_mix_with_same_number_of_lines(lyrics_editor):
    lyrics1 = Lyrics.with_text('lyrics 1 line 2\nlyrics 1 line 2\n\nlyrics 1 line 3\n\n')
    lyrics2 = Lyrics.with_text('lyrics 2 line 1\nlyrics 2 line 2\n\nlyrics 2 line 3\n\n')

    mixed_lyrics = lyrics_editor.mix(lyrics1, lyrics2)

    expected_paragraphs = Paragraphs.from_text('lyrics 1 line 2\nlyrics 2 line 1\nlyrics 1 line 2\nlyrics 2 line 2\nlyrics 1 line 3\nlyrics 2 line 3\n\n')

    assert mixed_lyrics.paragraphs == expected_paragraphs


def test_mix_with_first_lyrics_with_2_lines_and_second_lyrics_with_1_line(lyrics_editor):
    lyrics1 = Lyrics.with_text('lyrics 1 line 1\nlyrics 1 line 2')
    lyrics2 = Lyrics.with_text('lyrics 2 line 1')

    mixed_lyrics = lyrics_editor.mix(lyrics1, lyrics2)

    expected_paragraphs = Paragraphs.from_text('lyrics 1 line 1\nlyrics 2 line 1')

    assert mixed_lyrics.paragraphs == expected_paragraphs


def test_mix_with_first_lyrics_with_1_line_and_second_lyrics_with_2_lines(lyrics_editor):
    lyrics1 = Lyrics.with_text('lyrics 1 line 1')
    lyrics2 = Lyrics.with_text('lyrics 2 line 1\nlyrics 2 line 2')

    mixed_lyrics = lyrics_editor.mix(lyrics1, lyrics2)

    expected_paragraphs = Paragraphs.from_text('lyrics 1 line 1\nlyrics 2 line 1')

    assert mixed_lyrics.paragraphs == expected_paragraphs


def test_mix_with_first_paragraph_containing_two_lines_and_second_paragraph_containing_one_line(lyrics_editor):
    lyrics1 = Lyrics.with_text('lyrics 1 line 1\nlyrics 1 line 2\n\nlyrics 1 line 3')
    lyrics2 = Lyrics.with_text('lyrics 2 line 1\nlyrics 2 line 2\n\nlyrics 2 line 3')

    mixed_lyrics = lyrics_editor.mix(lyrics1, lyrics2)

    expected_paragraphs = Paragraphs.from_text('lyrics 1 line 1\nlyrics 2 line 1\nlyrics 1 line 2\nlyrics 2 line 2\nlyrics 1 line 3\nlyrics 2 line 3\n\n')

    assert mixed_lyrics.paragraphs == expected_paragraphs


def test_mix_with_first_paragraph_containing_one_line_and_second_paragraph_containing_two_lines(lyrics_editor):
    lyrics1 = Lyrics.with_text('lyrics 1 line 1\n\nlyrics 1 line 2\nlyrics 1 line 3')
    lyrics2 = Lyrics.with_text('lyrics 2 line 1\n\nlyrics 2 line 2\nlyrics 2 line 3')

    mixed_lyrics = lyrics_editor.mix(lyrics1, lyrics2)

    expected_paragraphs = Paragraphs.from_text('lyrics 1 line 1\nlyrics 2 line 1\nlyrics 1 line 2\nlyrics 2 line 2\nlyrics 1 line 3\nlyrics 2 line 3\n\n')

    assert mixed_lyrics.paragraphs == expected_paragraphs
