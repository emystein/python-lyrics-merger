import re
from songs.model import SongTitle
from lyrics_mixer.mix_commands import ArtistsMixCommand, SongTitlesMixCommand

prefixes = r"(?:" + ".*mezcl.|.*combin.|.*mix" + r")?\s?"
connectors = "(?:, | y | and | con | with )"


class SongTitlesSplitter:
    def split(self, text):
        title = self.optionally_quoted("([^'\"]+)")
        match = re.match(prefixes + title + connectors + title, text)
        return list(match.groups())

    def optionally_quoted(self, pattern):
        optional_quote = "['\"]?"
        return optional_quote + pattern + optional_quote


class SongTitlesParser:
    def parse(self, text):
        splitter = SongTitlesSplitter()
        split_text = splitter.split(text)

        all_mix_commands = [
            SongTitlesMixCommand(split_text),
            ArtistsMixCommand(split_text)
        ]

        return next(command for command in all_mix_commands if command.accepts(text))
