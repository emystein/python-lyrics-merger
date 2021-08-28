import pytest
from lyrics_mixer.lyrics_mixer import ParagraphInterleaveLyricsMix
from songs.model import SongTitle, Song, Lyrics

song_title1 = SongTitle('artist1', 'title1')
song_title2 = SongTitle('artist2', 'title2')


@pytest.fixture
def lyrics_editor():
    return ParagraphInterleaveLyricsMix()


def test_mix_with_same_number_of_paragraphs(lyrics_editor):
    song1 = Song(song_title1, Lyrics('lyrics 1 line 1\nlyrics 1 line 2\n\nlyrics 1 line 3'))
    song2 = Song(song_title2, Lyrics('lyrics 2 line 1\nlyrics 2 line 2\n\nlyrics 2 line 3'))

    mixed_lyrics = lyrics_editor.mix(song1, song2)

    expected_paragraphs = [
        'lyrics 1 line 1\nlyrics 1 line 2',
        'lyrics 2 line 1\nlyrics 2 line 2',
        'lyrics 1 line 3',
        'lyrics 2 line 3'
    ]

    assert mixed_lyrics.text == '\n\n'.join([paragraph for paragraph in expected_paragraphs])


def test_mix_with_first_lyrics_with_2_paragraphs_and_second_lyrics_with_1_paragraph(lyrics_editor):
    song1 = Song(song_title1, Lyrics('lyrics 1 line 1\n\nlyrics 1 line 2'))
    song2 = Song(song_title2, Lyrics('lyrics 2 line 1'))

    mixed_lyrics = lyrics_editor.mix(song1, song2)

    expected_paragraphs = [
        'lyrics 1 line 1',
        'lyrics 2 line 1'
    ]

    assert mixed_lyrics.text == '\n\n'.join([paragraph for paragraph in expected_paragraphs])


def test_mix_with_first_lyrics_with_1_paragraph_and_second_lyrics_with_2_paragraphs(lyrics_editor):
    song1 = Song(song_title1, Lyrics('lyrics 1 line 1'))
    song2 = Song(song_title2, Lyrics('lyrics 2 line 1\n\nlyrics 2 line 2'))

    mixed_lyrics = lyrics_editor.mix(song1, song2)

    expected_paragraphs = [
        'lyrics 1 line 1',
        'lyrics 2 line 1'
    ]

    assert mixed_lyrics.text == '\n\n'.join([paragraph for paragraph in expected_paragraphs])
