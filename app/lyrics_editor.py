from app.lyrics import Lyrics
from app.random_lyrics_merger import MergedLyrics

class LyricsEditor(object):
	def merge(self, song1, song2):
		lyrics1 = Lyrics(song1.lyrics)
		lyrics2 = Lyrics(song2.lyrics)
		# see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
		paragraphs = [val for pair in zip(lyrics1.paragraphs(), lyrics2.paragraphs()) for val in pair]
		return MergedLyrics(song1, song2, paragraphs)
