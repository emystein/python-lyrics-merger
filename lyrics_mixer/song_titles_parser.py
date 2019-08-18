import re
from songs.model import SongTitle

def parse(text):
	match = re.match(r"(.*)(?:, | y )(.*)", text)
	titles = list(match.groups())
	return SongTitlesParseResult(titles)


class SongTitlesParseResult(object):
	def __init__(self, titles):
		self.song_titles = list(map(lambda title: self.split_artist_and_title(title), titles))
	
	def split_artist_and_title(self, artist_and_title):
		artist, title = artist_and_title.split('-')
		return SongTitle(artist, title)