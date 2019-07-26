import pytest
from wikia.song_url_parser import WikiaSongUrlParser

def test_get_song_title_from_url():
	parser = WikiaSongUrlParser()
	song_title = parser.parse_url("https://lyrics.fandom.com/wiki/Led_Zeppelin:Stairway_To_Heaven")
	assert song_title.artist == 'Led Zeppelin'
	assert song_title.title == 'Stairway To Heaven'

def test_get_song_info_from_escaped_url():
	parser = WikiaSongUrlParser()
	song_title = parser.parse_url("https://lyrics.fandom.com/wiki/Pablo_Guerrero:Para%C3%ADso_Ahora")
	assert song_title.artist == 'Pablo Guerrero'
	assert song_title.title == 'Paraíso Ahora'