import pytest
from lyrics_mixer.lyrics_mixer import LyricsMixer, ParagraphInterleaveLyricsMixStrategy, MixedLyrics
from wikia.lyrics import WikiaLyrics


@pytest.fixture
def mixer():
    return LyricsMixer(WikiaLyrics(), ParagraphInterleaveLyricsMixStrategy())
