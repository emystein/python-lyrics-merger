import re
from songs.model import SongTitle, EmptySongTitle
from lyrics_mixer.mix_commands import ParsedSongTitles, ParsedArtists


class SongTitlesSplitter:
    @staticmethod
    def prefixes():
        return ['', 'mezclá ', 'combiná ', 'mix ']

    @staticmethod
    def connectors():
        return [', ', ' y ', ' and ', ' con ', ' with ']

    def split(self, text):
        prefixes = r"(?:" + ".*mezcl.|.*combin.|.*mix" + r")?\s?"
        connectors = "(?:, | y | and | con | with )"
        title = self.optionally_quoted("([^'\"]+)")
        match = re.match(prefixes + title + connectors + title, text)
        return list(match.groups())

    def optionally_quoted(self, pattern):
        optional_quote = "['\"]?"
        return optional_quote + pattern + optional_quote


class SongTitlesParser:
    def __init__(self, titles_splitter):
        self.titles_splitter = titles_splitter

    def parse(self, text):
        split_text = self.titles_splitter.split(text)

        parse_structures = [ParsedSongTitles(split_text), ParsedArtists(split_text)]

        return next(parsed for parsed in parse_structures if parsed.accepts(split_text))
