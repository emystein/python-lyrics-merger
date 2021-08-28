import pytest
from lyrics_mixer.lyrics_mixer import MixedLyrics
from songs.model import SongTitle

def test_mixed_lyrics_lines():
    song_title1 = SongTitle('Artist1', 'Title 1')
    song_title2 = SongTitle('Artist2', 'Title 2')
    song_titles = [song_title1, song_title2]

    paragraphs = [
        'lyrics 1 line 1\nlyrics 1 line 2',
        'lyrics 2 line 1\nlyrics 2 line 2',
        'lyrics 1 line 3',
        'lyrics 2 line 3'
    ]

    mixed_lyrics = MixedLyrics(song_titles, paragraphs)

    assert mixed_lyrics.lines == [
        'lyrics 1 line 1',
        'lyrics 1 line 2',
        'lyrics 2 line 1',
        'lyrics 2 line 2',
        'lyrics 1 line 3',
        'lyrics 2 line 3',
    ]



