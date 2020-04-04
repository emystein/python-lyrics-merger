import re
from songs.model import SongTitle, EmptySongTitle, ArtistOnlySongTitle

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


class ParsedSongTitles:
    def __init__(self, split_text):
        if self.accepts(split_text):
            artist, title = split_text[0].split(' - ')
            self.song_title1 = SongTitle(artist, title)
            artist, title = split_text[1].split(' - ')
            self.song_title2 = SongTitle(artist, title)
        else:
            self.song_title1 = EmptySongTitle()
            self.song_title2 = EmptySongTitle()
    
    def accepts(self, split_text):
        return '-' in split_text[0]


class ParsedArtists:
    def __init__(self, split_text):
        if self.accepts(split_text):
            self.song_title1 = ArtistOnlySongTitle(split_text[0])
            self.song_title2 = ArtistOnlySongTitle(split_text[1])
        else:
            self.song_title1 = EmptySongTitle()
            self.song_title2 = EmptySongTitle()

    def accepts(self, split_text):
        return '-' not in split_text[0]


