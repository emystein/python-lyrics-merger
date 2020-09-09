import pytest
from lyrics_mixer.lyrics_mixer import LyricsMixer, ParagraphInterleaveLyricsMixStrategy, MixedLyrics
from wikia.lyrics_api_client import WikiaLyricsApiClient


@pytest.fixture
def mixer():
    return LyricsMixer(WikiaLyricsApiClient(), ParagraphInterleaveLyricsMixStrategy())
