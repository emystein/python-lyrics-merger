import pytest
import requests
import lyricwikia
import urllib

def test_get_random_lyrics_from_lyrics_wikia():
	r = requests.get('https://lyrics.fandom.com/wiki/Special:RandomInCategory/Song')
	print('\n')
	print('Lyrics URL: ' + r.url)
	unescaped_url = urllib.parse.unquote(r.url)
	artist, song = unescaped_url.rsplit('/', 1)[-1].split(':', 2)
	print('Artist: ' + artist + ', Song: ' + song)
	lyrics = lyricwikia.get_lyrics(artist, song)
	print('Lyrics: \n' + lyrics)

	assert (lyrics != "")

