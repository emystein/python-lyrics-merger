import random


class SongTitle:
    @staticmethod
    def empty():
        return SongTitle('', '')

    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    def is_empty(self):
        return self.artist == '' and self.title == ''

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)

    def __str__(self):
        return self.artist + ' - ' + self.title


class Song:
    @staticmethod
    def random_from(songs):
        if len(songs) > 0:
            return Song.copy(random.choice(songs))
        else:
            return Song.none()

    @staticmethod
    def none():
        return Song(SongTitle.empty(), Lyrics.empty())

    @staticmethod
    def copy(another):
        return Song(another.title, another.lyrics)

    def __init__(self, title, lyrics):
        self.title = title
        self.lyrics = lyrics

    def has_lyrics(self):
        return self.lyrics.has_content()

    def __eq__(self, other):
        return self.title == other.title


class Lyrics:
    @staticmethod
    def empty():
        return Lyrics('')

    def __init__(self, text):
        self.text = text
        self.paragraphs = Paragraphs.from_text(text)
        self.lines = [line for paragraph in self.paragraphs for line in paragraph]

    def has_content(self):
        return self != Lyrics.empty()

    def __eq__(self, other):
        return self.text == other.text

    def __str__(self):
        return self.text


class Paragraphs:
    @staticmethod
    def from_text(text):
        return Paragraphs.from_list([Paragraph.from_plain(paragraph) for paragraph in text.split('\n\n')])

    @staticmethod
    def from_list(paragraphs):
        return [paragraph for paragraph in paragraphs if not paragraph.is_empty()]


class Paragraph:
    @staticmethod
    def from_plain(plain_paragraph):
        lines = [Line(text) for text in plain_paragraph.split('\n')]
        return Paragraph(lines)

    def __init__(self, lines):
        self.lines = [line for line in lines if not line.is_empty()]
        self.text = ''.join([line.text + '\n' for line in self.lines]) + '\n'

    def is_empty(self):
        return len(self.lines) == 0

    def __iter__(self):
        return iter(self.lines)

    def __eq__(self, other):
        return self.text == other.text

    def __str__(self):
        return self.text


class Line:
    def __init__(self, text):
        self.text = text

    def is_empty(self):
        return self.text == ''

    def __eq__(self, other):
        return self.text == other.text

    def __str__(self):
        return self.text
