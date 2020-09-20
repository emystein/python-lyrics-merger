from abc import abstractmethod
import re
from songs.model import SongTitle, SongTitlePair, ArtistTitle


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
        self.parsers = [FullTitlesParser(), ArtistsParser()]

    def parse(self, text):
        split_text = self.titles_splitter.split(text)

        return next(parser.parse_song_titles(split_text)
                    for parser in self.parsers
                    if parser.can_create_from(split_text[0]))


class FullTitlesParser:
    def parse_song_titles(self, split_text):
        song_title1 = self.parse_song_title(split_text[0])
        song_title2 = self.parse_song_title(split_text[1])
        return ParsedFullTitles(song_title1, song_title2)

    def parse_song_title(self, text):
        if self.can_create_from(text):
            return self.create_from(text)
        else:
            return SongTitle.empty()

    def can_create_from(self, text):
        return '-' in text

    def create_from(self, text):
        artist, title = text.split('-')
        return SongTitle(artist, title)


class ParsedFullTitles(SongTitlePair):
    def mix_using(self, lyrics_mixer):
        return lyrics_mixer.mix_two_specific_lyrics(self.song_title1, self.song_title2)


class ArtistsParser:
    def parse_song_titles(self, split_text):
        song_title1 = self.parse_song_title(split_text[0])
        song_title2 = self.parse_song_title(split_text[1])
        return ParsedArtists(song_title1, song_title2)

    def parse_song_title(self, text):
        if self.can_create_from(text):
            return self.create_from(text)
        else:
            return SongTitle.empty()

    def can_create_from(self, text):
        return '-' not in text

    def create_from(self, text):
        return ArtistTitle(text)


class ParsedArtists(SongTitlePair):
    def mix_using(self, lyrics_mixer):
        return lyrics_mixer.mix_random_lyrics_by_artists(self.song_title1.artist, self.song_title2.artist)
