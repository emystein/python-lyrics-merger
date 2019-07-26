import pytest
from app.wikia_song_url_parser import WikiaSongUrlParser

def test_get_song_title_from_url():
	parser = WikiaSongUrlParser()
	song_title = parser.parse_url("https://lyrics.fandom.com/wiki/Led_Zeppelin:Stairway_To_Heaven")
	assert song_title.artist == 'Led_Zeppelin'
	assert song_title.title == 'Stairway_To_Heaven'
