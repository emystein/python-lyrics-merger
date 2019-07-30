import pytest
from wikia.random_song_url_parser import WikiaRandomSongUrlParser


def test_parse_random_song_url():
	parser = WikiaRandomSongUrlParser()
	song = parser.get_random_song()
	assert song.artist != ''
	assert song.title != ''
