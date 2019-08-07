import re

class ArtistsParser(object):
	
	def parse(self, text):
		prefixes = ".*mezcl.|.*combin.|.*mix"
		artist = self.optionally_quoted("([^'\"]+)")
		match = re.match(r"(?:" + prefixes + r")?\s?" + artist + " (?:y|and) " + artist, text)
		return ParseResult(artists = list(match.groups()))
	
	def optionally_quoted(self, pattern):
		optional_quote = "['\"]?"
		return optional_quote + pattern + optional_quote
	
	
	
class ParseResult(object):
	def __init__(self, artists):
		self.artists = artists
		self.artist1 = artists[0]
		self.artist2 = artists[1]