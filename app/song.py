class Song(object):
    def __init__(self, artist, title, lyrics):
        self.title = SongTitle(artist, title)
        self.lyrics = lyrics


class SongTitle(object):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)

    def __str__(self):
        return self.artist + ' - ' + self.title

    # def __add__(self, other):
    #     return self.__str__() + other