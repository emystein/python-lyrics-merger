import re
from songs.model import SongTitle
from lyrics_mixer.mix_commands import ArtistsMixCommand, SongTitlesMixCommand


class ArtistsParser:
    def parse(self, text):
        prefixes = ".*mezcl.|.*combin.|.*mix"
        artist = self.optionally_quoted("([^'\"]+)")
        match = re.match(r"(?:" + prefixes + r")?\s?" +
                         artist + " (?:y|con|and|with) " + artist, text)
        return ArtistsMixCommand(artists=list(match.groups()))

    def optionally_quoted(self, pattern):
        optional_quote = "['\"]?"
        return optional_quote + pattern + optional_quote


class SongTitlesParser:
	def parse(self, text):
		match = re.match(r"(.*)(?:, | y )(.*)", text)
		titles = list(match.groups())
		if '-' in text:
			return SongTitlesMixCommand(titles)
		else:
			return ArtistsMixCommand(titles)

