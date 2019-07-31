from app.lyrics import Lyrics

class Song(object):
    def __init__(self, artist, title, lyrics_text):
        self.title = SongTitle(artist, title)
        self.lyrics = Lyrics(lyrics_text)


class SongTitle(object):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)

    def __str__(self):
        return self.artist + ' - ' + self.title