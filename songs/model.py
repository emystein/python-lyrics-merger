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
        return Song('', SongTitle.empty(), Lyrics.empty())

    @staticmethod
    def copy(another):
        return Song(another.artist, another.title, another.lyrics)

    def __init__(self, artist, title, lyrics):
        self.artist = artist
        self.title = title
        self.lyrics = lyrics

    def is_empty(self):
        return self.artist == '' and self.title == SongTitle.empty()

    def has_lyrics(self):
        return self.lyrics.has_content()

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)


class SongTitle:
    @staticmethod
    def empty():
        return SongTitle('', '')

    def __init__(self, artist, title):
        self.artist = artist.strip()
        self.title = title.strip()

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)

    def __str__(self):
        return self.artist + ' - ' + self.title


class ArtistTitle:
    def __init__(self, artist):
        self.artist = artist.strip()
        self.title = ''

    def __eq__(self, other):
        return self.artist == other.artist

    def __str__(self):
        return self.artist 


class SongTitlePair:
    def __init__(self, song_title1, song_title2):
        self.song_title1 = song_title1
        self.song_title2 = song_title2

    def __str__(self):
        return f"{self.song_title1}, {self.song_title2}"


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
