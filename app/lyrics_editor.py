class LyricsEditor(object):
	def merge_lyrics(self, lyrics1, lyrics2):
		# see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
		return [val for pair in zip(lyrics1.paragraphs(), lyrics2.paragraphs()) for val in pair]
