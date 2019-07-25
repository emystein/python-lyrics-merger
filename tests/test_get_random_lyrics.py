import pytest
from app.random_lyrics_downloader import RandomLyricsDownloader

def test_get_random_lyrics_from_lyrics_wikia():
	random_lyrics_url = 'https://lyrics.fandom.com/wiki/special:randomincategory/Song'
	downloader = RandomLyricsDownloader(random_lyrics_url)
	lyrics = downloader.download_next()
	assert (lyrics != "")

