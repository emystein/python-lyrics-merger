import pytest
from songs.model import SongTitle
from wikia.song_url_parser import WikiaSongUrlParser


@pytest.fixture
def parser():
	return WikiaSongUrlParser()


def test_parse_random_song_url(parser):
	song = parser.get_random_song()
	assert song.artist != ''
	assert song.title != ''


def test_get_song_title_from_url(parser):
	song_title = parser.parse_url("https://lyrics.fandom.com/wiki/Led_Zeppelin:Stairway_To_Heaven")
	assert song_title == SongTitle('Led Zeppelin', 'Stairway To Heaven')


def test_get_song_info_from_escaped_url(parser):
	song_title = parser.parse_url("https://lyrics.fandom.com/wiki/Pablo_Guerrero:Para%C3%ADso_Ahora")
	assert song_title == SongTitle('Pablo Guerrero', 'Paraíso Ahora')


def test_get_song_title_from_url_including_slash_in_title(parser):
	song_title = parser.parse_url("https://lyrics.fandom.com/wiki/Michael_W._Smith:The_Tribute/Agnus_Dei")
	assert song_title == SongTitle('Michael W. Smith', 'The Tribute/Agnus Dei')