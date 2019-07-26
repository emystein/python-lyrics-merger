import pytest
from app.lyrics_downloader import LyricsDownloader
from wikia.song_url_parser import WikiaSongUrlParser
from wikia.lyrics_api_adapter import WikiaLyricsAdapter


def test_get_random_lyrics_from_wikia():
	random_lyrics_url = 'https://lyrics.fandom.com/wiki/special:randomincategory/Song'
	downloader = LyricsDownloader(random_lyrics_url, WikiaSongUrlParser(), WikiaLyricsAdapter())
	song = downloader.download_next()
	print('Artist: ' + song.artist + ', Title: ' + song.title + '\nLyrics: \n' + song.lyrics)
	assert (song.lyrics != "")
