class SongTitle(object):
	def __init__(self, artist, title):
		self.artist = artist
		self.title = title

	def __eq__(self, other):
		return (self.artist == other.artist) and (self.title == other.title)