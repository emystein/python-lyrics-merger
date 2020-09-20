import pytest
from lyrics_providers.azlyrics import SongTitle


@pytest.mark.slow_integration_test
def test_random():
	artist, title = SongTitle.random()

	assert artist != ''
	assert title != ''
