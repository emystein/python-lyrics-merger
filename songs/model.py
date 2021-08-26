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

    def has_content(self):
        return self != Lyrics.empty()

    def lines(self):
        return self.text.split('\n')

    def paragraphs(self):
        return self.text.split('\n\n')

    def __eq__(self, other):
        return self.text == other.text

    def __str__(self):
        return self.text


def plain_paragraphs_from(text):
    return text.split('\n\n')


def lines_from(plain_paragraph):
    return [Line(line_text) for line_text in plain_paragraph.split('\n')]


def paragraph_from(plain_paragraph):
    return Paragraph(lines_from(plain_paragraph))


class Paragraphs:
    def __init__(self, text):
        self.paragraphs = [
            paragraph_from(plain_paragraph) for plain_paragraph in plain_paragraphs_from(text)
        ]

    def __getitem__(self, index):
        return self.paragraphs[index]

    def __eq__(self, other):
        return self.paragraphs == other.paragraphs

    def __str__(self):
        return str([str(paragraph) + '\n\n' for paragraph in self.paragraphs])


class Paragraph:
    def __init__(self, lines):
        self.lines = lines

    def __eq__(self, other):
        return self.lines == other.lines

    def __str__(self):
        return str([str(line) + '\n' for line in self.lines])


class Line:
    def __init__(self, text):
        self.text = text

    def __eq__(self, other):
        return self.text == other.text

    def __str__(self):
        return self.text
