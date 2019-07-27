class LyricsEditor(object):
	def split_paragraphs(self, lyrics):
		return lyrics.split('\n\n')

	def merge_lyrics(self, lyrics1, lyrics2):
		split1 = self.split_paragraphs(lyrics1)
		split2 = self.split_paragraphs(lyrics2)
		# see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
		return [val for pair in zip(split1, split2) for val in pair]
