import requests
import lyricwikia
import urllib
from app.song import Song

class RandomLyricsDownloader(object):
	def __init__(self, random_lyrics_url):
	    self.random_lyrics_url = random_lyrics_url

	def download_next(self):
		r = requests.get(self.random_lyrics_url)
		print('\nLyrics URL: ' + r.url)
		unescaped_url = urllib.parse.unquote(r.url)
		artist, title = unescaped_url.rsplit('/', 1)[-1].split(':', 2)
		print('Artist: ' + artist + ', Song: ' + title)
		lyrics = lyricwikia.get_lyrics(artist, title)
		song = Song(artist, title, lyrics)
		print('Lyrics: \n' + song.lyrics)
		return song.lyrics
