import pytest
from app.lyrics_editor import LyricsEditor
from app.lyrics import Lyrics

@pytest.fixture
def lyrics_editor():
    return LyricsEditor()

def test_merge_lyrics_with_same_number_of_paragraphs(lyrics_editor):
    lyrics1 = Lyrics('lyrics 1 first paragraph\n\nlyrics 1 second paragraph')
    lyrics2 = Lyrics('lyrics 2 first paragraph\n\nlyrics 2 second paragraph')
    merged_lyrics = lyrics_editor.merge_lyrics(lyrics1, lyrics2)
    assert merged_lyrics == ['lyrics 1 first paragraph', 'lyrics 2 first paragraph',
                             'lyrics 1 second paragraph', 'lyrics 2 second paragraph']


def test_merge_lyrics_with_first_lyrics_with_2_paragraphs_and_second_lyrics_with_1_paragraph(lyrics_editor):
    lyrics1 = Lyrics('lyrics 1 first paragraph\n\nlyrics 1 second paragraph')
    lyrics2 = Lyrics('lyrics 2 first paragraph')
    merged_lyrics = lyrics_editor.merge_lyrics(lyrics1, lyrics2)
    assert merged_lyrics == ['lyrics 1 first paragraph', 'lyrics 2 first paragraph']


def test_merge_lyrics_with_first_lyrics_with_1_paragraph_and_second_lyrics_with_2_paragraphs(lyrics_editor):
    lyrics1 = Lyrics('lyrics 1 first paragraph')
    lyrics2 = Lyrics('lyrics 2 first paragraph\n\nlyrics 2 second paragraph')
    merged_lyrics = lyrics_editor.merge_lyrics(lyrics1, lyrics2)
    assert merged_lyrics == ['lyrics 1 first paragraph', 'lyrics 2 first paragraph']
