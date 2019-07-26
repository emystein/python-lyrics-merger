import pytest
from app.random_lyrics_downloader import RandomLyricsDownloader


def test_get_random_lyrics_from_wikia():
	random_lyrics_url = 'https://lyrics.fandom.com/wiki/special:randomincategory/Song'
	downloader = RandomLyricsDownloader(random_lyrics_url)
	song = downloader.download_next()
	print('Artist: ' + song.artist + ', Title: ' + song.title + '\nLyrics: \n' + song.lyrics)
	assert (song.lyrics != "")
