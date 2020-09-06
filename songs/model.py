import random

class Song:
    @staticmethod
    def random_from(list):
        if len(list) > 0:
            return Song.copy(random.choice(list))
        else:
            return Song.none()

    @staticmethod
    def none():
        return Song('', '', '')

    @staticmethod
    def copy(another):
        return Song(another.artist, another.title, another.lyrics)

    def __init__(self, artist, title, lyrics_text):
        self.artist = artist
        self.title = title
        self.lyrics = Lyrics(lyrics_text)

    def full_title(self):
        return self.artist + ' - ' + self.title

    def has_lyrics(self):
        return self.lyrics != Lyrics.empty()

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)
    
    def is_empty(self):
        return self.artist == '' and self.title == ''


class SongTitle:
    @staticmethod
    def empty():
        return SongTitle('', '')

    @staticmethod
    def artist_only(artist):
        return SongTitle(artist, '')

    def __init__(self, artist, title):
        self.artist = artist.strip()
        self.title = title.strip()

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)

    def __str__(self):
        return self.artist + ' - ' + self.title


class Lyrics:
    @staticmethod
    def empty():
        return Lyrics('')

    def __init__(self, text):
        self.text = text

    def lines(self):
        return self.text.split('\n')

    def paragraphs(self):
        return self.text.split('\n\n')

    def __str__(self):
        return self.text

    def __eq__(self, other):
        return (self.text == other.text)
