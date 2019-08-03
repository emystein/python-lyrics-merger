import pytest
from lyrics_mixer.lyrics_mixer import LineInterleaveLyricsEditor
from lyrics_mixer.song import Song
from lyrics_mixer.song import Lyrics

@pytest.fixture
def lyrics_editor():
    return LineInterleaveLyricsEditor()

def test_interleave_lyrics_with_same_number_of_lines(lyrics_editor):
    song1 = Song('artist1', 'title1', 'lyrics 1 first line\nlyrics 1 second line')
    song2 = Song('artist2', 'title2', 'lyrics 2 first line\nlyrics 2 second line')
    merged_lyrics = lyrics_editor.interleave_lyrics(song1, song2)
    assert merged_lyrics.lines == ['lyrics 1 first line', 'lyrics 2 first line', 'lyrics 1 second line', 'lyrics 2 second line']


def test_interleave_lyrics_with_first_lyrics_with_2_lines_and_second_lyrics_with_1_line(lyrics_editor):
    song1 = Song('artist1', 'title1', 'lyrics 1 first line\nlyrics 1 second line')
    song2 = Song('artist2', 'title2', 'lyrics 2 first line')
    merged_lyrics = lyrics_editor.interleave_lyrics(song1, song2)
    assert merged_lyrics.lines == ['lyrics 1 first line', 'lyrics 2 first line']


def test_interleave_lyrics_with_first_lyrics_with_1_line_and_second_lyrics_with_2_lines(lyrics_editor):
    song1 = Song('artist1', 'title1', 'lyrics 1 first line')
    song2 = Song('artist2', 'title2', 'lyrics 2 first line\nlyrics 2 second line')
    merged_lyrics = lyrics_editor.interleave_lyrics(song1, song2)
    assert merged_lyrics.lines == ['lyrics 1 first line', 'lyrics 2 first line']


def test_interleave_lyrics_with_first_paragraph_containing_one_line_and_second_paragraph_containing_two_lines(lyrics_editor):
    song1 = Song('artist1', 'title1', 'lyrics 1 first line\nlyrics 1 second line\n\nlyrics 1 third line')
    song2 = Song('artist2', 'title2', 'lyrics 2 first line\nlyrics 2 second line\n\nlyrics 2 third line')
    merged_lyrics = lyrics_editor.interleave_lyrics(song1, song2)
    assert merged_lyrics.lines == ['lyrics 1 first line', 'lyrics 2 first line', 'lyrics 1 second line', 'lyrics 2 second line', '', '', 'lyrics 1 third line', 'lyrics 2 third line']
    assert merged_lyrics.paragraphs == ['lyrics 1 first line\nlyrics 2 first line\nlyrics 1 second line\nlyrics 2 second line', 'lyrics 1 third line\nlyrics 2 third line']


def test_interleave_lyrics_with_first_paragraph_containing_two_lines_and_second_paragraph_containing_one_line(lyrics_editor):
    song1 = Song('artist1', 'title1', 'lyrics 1 first line\n\nlyrics 1 second line\nlyrics 1 third line')
    song2 = Song('artist2', 'title2', 'lyrics 2 first line\n\nlyrics 2 second line\nlyrics 2 third line')
    merged_lyrics = lyrics_editor.interleave_lyrics(song1, song2)
    assert merged_lyrics.lines == ['lyrics 1 first line', 'lyrics 2 first line', '', '', 'lyrics 1 second line', 'lyrics 2 second line', 'lyrics 1 third line', 'lyrics 2 third line']
    assert merged_lyrics.paragraphs == ['lyrics 1 first line\nlyrics 2 first line', 'lyrics 1 second line\nlyrics 2 second line\nlyrics 1 third line\nlyrics 2 third line']
