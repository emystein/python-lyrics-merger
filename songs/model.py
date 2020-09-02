import random

class Song:
    @staticmethod
    def random_from(list):
        if len(list) > 0:
            return Song.copy(random.choice(list))
        else:
            return NullSong()

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
        return self.lyrics != EmptyLyrics()

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)

class NullSong:
    def __init__(self):
        self.artist = ''
        self.title = ''
        self.lyrics = EmptyLyrics()
    
    def __eq__(self, other):
        return (self.title == other.title) and (self.lyrics == other.lyrics)


class SongTitle:
    def __init__(self, artist, title):
        self.artist = artist.strip()
        self.title = title.strip()

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)

    def __str__(self):
        return self.artist + ' - ' + self.title


class EmptySongTitle(SongTitle):
    def __init__(self):
        return

    def __eq__(self, other):
        return self.__class__ == other.__class__

    def __str__(self):
        return 'Empty Song Title'


class ArtistOnlySongTitle(SongTitle):
    def __init__(self, artist):
        self.artist = artist.strip()
        self.title = None

    def __eq__(self, other):
        return other.__class__ == self.__class__ and (other.artist == self.artist) 


class Lyrics:
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


class EmptyLyrics(Lyrics):
    def __init__(self):
        super().__init__('')

