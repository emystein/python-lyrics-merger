import logging
import lyricwikia
import songs.model 
from wikia.urls import random_song_url, song_title_from


logger = logging.getLogger()


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
        return songs.model.Song.random_from(self.all_songs())


class SongTitle:
    @staticmethod
    def random():
        return SongTitle.from_url(random_song_url())

    @staticmethod
    def from_url(url):
        artist, title = song_title_from(url)
        return songs.model.SongTitle(artist, title)


class Song:
    @staticmethod
    def entitled(title):
        logger.info(f'Retrieving song: {str(title)}')

        remote_song = lyricwikia.Song(title.artist, title.title)

        return songs.model.Song(remote_song.artist, remote_song.title, remote_song.lyrics)
