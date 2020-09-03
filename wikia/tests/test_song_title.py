import pytest
from songs.model import SongTitle
import wikia.song_title


def test_parse_random_song_url():
	title = wikia.song_title.random_song_title()

	assert title.artist != ''
	assert title.title != ''


@pytest.mark.parametrize("song_url,expected_artist,expected_song", 
[
	("https://lyrics.fandom.com/wiki/Led_Zeppelin:Stairway_To_Heaven", 'Led Zeppelin', 'Stairway To Heaven'), 
	("https://lyrics.fandom.com/wiki/Pablo_Guerrero:Para%C3%ADso_Ahora", 'Pablo Guerrero', 'Paraíso Ahora'),
	("https://lyrics.fandom.com/wiki/Michael_W._Smith:The_Tribute/Agnus_Dei", 'Michael W. Smith', 'The Tribute/Agnus Dei')
])
def test_parse_url(song_url, expected_artist, expected_song):
	title = wikia.song_title.parse_url(song_url)

	assert title == SongTitle(expected_artist, expected_song)
