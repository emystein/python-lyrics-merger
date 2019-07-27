import pytest
from app.lyrics_downloader import RandomLyricsDownloader
from wikia.song_url_parser import WikiaSongUrlParser
from wikia.lyrics_api_adapter import WikiaLyricsApiClient


def test_get_random_lyrics_from_wikia():
	random_lyrics_url = 'https://lyrics.fandom.com/wiki/special:randomincategory/Song'
	downloader = RandomLyricsDownloader(random_lyrics_url, WikiaSongUrlParser(), WikiaLyricsApiClient())
	song = downloader.download_random_lyrics()
	print('Artist: ' + song.artist + ', Title: ' + song.title + '\nLyrics: \n' + song.lyrics)
	assert (song.lyrics != "")

def test_get_random_lyrics_by_artist_from_wikia():
	random_lyrics_url = 'https://lyrics.fandom.com/wiki/special:randlyrics_api_client'
	downloader = RandomLyricsDownloader(random_lyrics_url, WikiaSongUrlParser(), WikiaLyricsApiClient())
	lyrics = downloader.download_random_lyrics_by_artist('Led Zeppelin')
	assert (lyrics != "")