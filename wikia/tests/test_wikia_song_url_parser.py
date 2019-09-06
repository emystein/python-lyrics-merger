import pytest
from songs.model import SongTitle
import wikia.song_url_parser


def test_parse_random_song_url():
	song = wikia.song_url_parser.get_random_song()
	assert song.artist != ''
	assert song.title != ''


def test_get_song_title_from_url():
	song_title = wikia.song_url_parser.parse_url("https://lyrics.fandom.com/wiki/Led_Zeppelin:Stairway_To_Heaven")
	assert song_title == SongTitle('Led Zeppelin', 'Stairway To Heaven')


def test_get_song_info_from_escaped_url():
	song_title = wikia.song_url_parser.parse_url("https://lyrics.fandom.com/wiki/Pablo_Guerrero:Para%C3%ADso_Ahora")
	assert song_title == SongTitle('Pablo Guerrero', 'Paraíso Ahora')


def test_get_song_title_from_url_including_slash_in_title():
	song_title = wikia.song_url_parser.parse_url("https://lyrics.fandom.com/wiki/Michael_W._Smith:The_Tribute/Agnus_Dei")
	assert song_title == SongTitle('Michael W. Smith', 'The Tribute/Agnus Dei')