import random


class Song:
    @staticmethod
    def random_from(songs):
        if len(songs) > 0:
            return Song.copy(random.choice(songs))
        else:
            return Song.none()

    @staticmethod
    def none():
        return Song('', '', Lyrics.empty())

    @staticmethod
    def copy(another):
        return Song(another.artist, another.title, another.lyrics)

    def __init__(self, artist, title, lyrics):
        self.artist = artist
        self.title = title
        self.lyrics = lyrics

    def is_empty(self):
        return self.artist == '' and self.title == ''

    def has_lyrics(self):
        return self.lyrics.has_content()

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)


class SongTitlePair:
    def __init__(self, artist1, title1, artist2, title2):
        self.artist1 = artist1.strip()
        self.title1 = title1.strip()
        self.artist2 = artist2.strip()
        self.title2 = title2.strip()

    def __str__(self):
        return f"{self.artist1} - {self.title1}, {self.artist2} - {self.title2}"


class Lyrics:
    @staticmethod
    def empty():
        return Lyrics('')

    def __init__(self, text):
        self.text = text

    def has_content(self):
        return self.text != ''

    def lines(self):
        return self.text.split('\n')

    def paragraphs(self):
        return self.text.split('\n\n')

    def __eq__(self, other):
        return self.text == other.text

    def __str__(self):
        return self.text
