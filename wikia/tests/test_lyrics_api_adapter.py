import pytest
from wikia.lyrics_api_adapter import WikiaLyricsAdapter
import lyricwikia


def test_get_lyrics():
	lyrics_api_adapter = WikiaLyricsAdapter()

	lyrics = lyrics_api_adapter.get_lyrics('Led Zeppelin', 'Stairway To Heaven')

	assert lyrics == lyricwikia.get_lyrics('Led Zeppelin', 'Stairway To Heaven')