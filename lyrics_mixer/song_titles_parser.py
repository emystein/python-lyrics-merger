import re


class SongTitlePair:
    def __init__(self, artist1, title1, artist2, title2):
        self.artist1 = artist1.strip()
        self.title1 = title1.strip()
        self.artist2 = artist2.strip()
        self.title2 = title2.strip()

    def __str__(self):
        return f"{self.artist1} - {self.title1}, {self.artist2} - {self.title2}"


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

        return next(parser.parse_song_titles(split_text)
                    for parser in [FullTitlesParser(), ArtistsParser()]
                    if parser.can_create_from(split_text))


class FullTitlesParser:
    def can_create_from(self, split_text):
        return '-' in split_text[0]

    def parse_song_titles(self, split_text):
        artist1, title1 = split_text[0].split('-')
        artist2, title2 = split_text[1].split('-')
        return ParsedFullTitles(artist1, title1, artist2, title2)


class ParsedFullTitles(SongTitlePair):
    def mix_using(self, lyrics_mixer):
        return lyrics_mixer.mix_two_specific_lyrics(self.artist1, self.title1, self.artist2, self.title2)


class ArtistsParser:
    def can_create_from(self, split_text):
        return '-' not in split_text[0]

    def parse_song_titles(self, split_text):
        return ParsedArtists(split_text[0], split_text[1])


class ParsedArtists(SongTitlePair):
    def __init__(self, artist1, artist2):
        super().__init__(artist1, '', artist2, '')

    def mix_using(self, lyrics_mixer):
        return lyrics_mixer.mix_random_lyrics_by_artists(self.artist1, self.artist2)


