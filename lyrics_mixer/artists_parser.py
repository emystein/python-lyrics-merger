import re

class ArtistsParser(object):
	def parse(self, text):
		prefixes = "mezcl.|combin.|mix"
		optional_quote = "['\"]?"
		artist = optional_quote + "([^'\"]+)" + optional_quote
		match = re.match(r"(?:@lyricsmixer )?(?:" + prefixes + r")?\s?" + artist + " (?:y|and) " + artist, text)
		artists = list(match.groups())
		return ParseResult(artists)
	

class ParseResult(object):
	def __init__(self, artists):
		self.artists = artists
		self.artist1 = artists[0]
		self.artist2 = artists[1]