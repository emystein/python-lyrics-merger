import pytest
from wikia.model import SongTitle


@pytest.mark.vcr()
def test_random():
	title = SongTitle.random()

	assert title.artist != ''
	assert title.title != ''


@pytest.mark.parametrize("song_url,expected_artist,expected_song", 
[
	("https://lyrics.fandom.com/wiki/Led_Zeppelin:Stairway_To_Heaven", 'Led Zeppelin', 'Stairway To Heaven'), 
	("https://lyrics.fandom.com/wiki/Pablo_Guerrero:Para%C3%ADso_Ahora", 'Pablo Guerrero', 'Paraíso Ahora'),
	("https://lyrics.fandom.com/wiki/Michael_W._Smith:The_Tribute/Agnus_Dei", 'Michael W. Smith', 'The Tribute/Agnus Dei')
])
def test_parse_url(song_url, expected_artist, expected_song):
	title = SongTitle.from_url(song_url)

	assert title.artist == expected_artist
	assert title.title == expected_song
