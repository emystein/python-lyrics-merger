import pytest
from lyrics_mixer.lyrics_mixer import LyricsMixer, ParagraphInterleaveLyricsMixStrategy, MixedLyrics
from lyrics_mixer.lyrics_data_source import LyricsDataSource


@pytest.fixture
def mixer():
    return LyricsMixer(LyricsDataSource(), ParagraphInterleaveLyricsMixStrategy())
