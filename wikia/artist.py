import lyricwikia
from songs.model import Song

class Artist:
    @staticmethod
    def named(name):
        return Artist(name)

    def __init__(self, name):
        self.name = name

    def all_songs(self):
        artist = lyricwikia.Artist(self.name)

        songs = []

        for album in artist.albums:
            songs.extend(album.songs)

        return songs

    def random_song(self):
        return Song.random_from(self.all_songs())