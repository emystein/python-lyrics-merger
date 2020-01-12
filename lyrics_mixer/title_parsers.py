import re
from songs.model import SongTitle
from lyrics_mixer.mix_commands import ArtistsMixCommand, SongTitlesMixCommand

prefixes = r"(?:" + ".*mezcl.|.*combin.|.*mix" + r")?\s?"
connectors = "(?:, | y | and | con | with )"

class ArtistsSplitter:
    def split(self, text):
        artist = self.optionally_quoted("([^'\"]+)")
        match = re.match(prefixes + artist + connectors + artist, text)
        return list(match.groups())

    def optionally_quoted(self, pattern):
        optional_quote = "['\"]?"
        return optional_quote + pattern + optional_quote


class ArtistsParser:
    def parse(self, text):
        splitter = ArtistsSplitter()
        split_text = splitter.split(text)
        return ArtistsMixCommand(split_text)


class SongTitlesSplitter:
    def split(self, text):
        match = re.match(prefixes + "(.*)" + connectors + "(.*)", text)
        return list(match.groups())


class SongTitlesParser:
    def parse(self, text):
        splitter = SongTitlesSplitter()
        split_text = splitter.split(text)

        all_mix_commands = [SongTitlesMixCommand(split_text), ArtistsMixCommand(split_text)]

        return next(command for command in all_mix_commands if command.accepts(text))
