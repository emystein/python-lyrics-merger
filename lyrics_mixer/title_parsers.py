import re
from songs.model import SongTitle
from lyrics_mixer.mix_commands import ArtistsMixCommand, SongTitlesMixCommand

prefixes = r"(?:.*mezcl.|.*combin.|.*mix)?\s?"
connectors = r"(.*)(?:, | y | con | and | with )(.*)"


class ArtistsParser:
    def parse(self, text):
        artist = self.optionally_quoted("([^'\"]+)")
        match = re.match(prefixes + artist + connector + artist, text)
        return ArtistsMixCommand(artists=list(match.groups()))

    def optionally_quoted(self, pattern):
        optional_quote = "['\"]?"
        return optional_quote + pattern + optional_quote


class SongTitlesParser:
    def parse(self, text):
        match = re.match(prefixes + connectors, text)
        titles = list(match.groups())
        if '-' in text:
            return SongTitlesMixCommand(titles)
        else:
            return ArtistsMixCommand(titles)
