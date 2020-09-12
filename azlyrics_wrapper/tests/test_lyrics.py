import pytest
from azlyrics_wrapper.model import LazyLoadLyrics
from songs.tests.fixtures.song_titles import song_title1


def test_lazy_load_lyrics(song_title1):
  lyrics = LazyLoadLyrics(song_title1.artist, song_title1.title)

  assert lyrics.text != ''