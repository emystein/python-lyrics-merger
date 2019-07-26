import urllib
from app.song_title import SongTitle

class WikiaSongUrlParser(object):
	def parse_url(self, url):
		unescaped_url = urllib.parse.unquote(url)
		artist, title = unescaped_url.replace('_', ' ').rsplit('/', 1)[-1].split(':', 2)
		return SongTitle(artist, title)
