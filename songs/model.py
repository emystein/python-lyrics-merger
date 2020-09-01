class Song:
    def __init__(self, artist, title, lyrics_text):
        self.artist = artist
        self.title = SongTitle(artist, title)
        self.lyrics = Lyrics(lyrics_text)


class NullSong:
    def __init__(self):
        self.title = SongTitle('', '')
        self.lyrics = EmptyLyrics()
    
    def __eq__(self, other):
        return (self.title == other.title) and (self.lyrics == other.lyrics)


class InstrumentalSong(Song):
    def __init__(self, artist, title):
        self.title = SongTitle(artist, title)
        self.lyrics = EmptyLyrics()

    def __eq__(self, other):
        return type(self) == type(other) and (self.title == other.title)


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

