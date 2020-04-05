from abc import abstractmethod
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


class SongTitleFactory:
    @abstractmethod
    def accepts(self, split_text):
        pass

    def __init__(self, split_text):
        self.song_title1 = self.parse_song_title(split_text[0])
        self.song_title2 = self.parse_song_title(split_text[1])

    @abstractmethod
    def can_create_from(self, text):
        pass
    
    @abstractmethod
    def create_from(self, text):
        pass

    def create(self, can_create_from, create_from, text):
        if can_create_from(text):
            return create_from(text)
        else:
            return EmptySongTitle()

    def parse_song_title(self, text):
        return self.create(self.can_create_from, self.create_from, text)


class ParsedSongTitles(SongTitleFactory):
    def can_create_from(self, text):
        return '-' in text

    def create_from(self, text):
        artist, title = text.split('-')
        return SongTitle(artist, title)

    def accepts(self, split_text):
        return '-' in split_text[0]


class ParsedArtists(SongTitleFactory):
    def can_create_from(self, text):
        return '-' not in text

    def create_from(self, text):
        return ArtistOnlySongTitle(text)

    def accepts(self, split_text):
        return '-' not in split_text[0]
