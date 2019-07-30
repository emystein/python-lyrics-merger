from app.song_title import SongTitle

class Song(object):
	def __init__(self, artist, title, lyrics):
		self.title = SongTitle(artist, title)
		self.lyrics = lyrics
