import logging
import lyricwikia
import random
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
        all_songs = self.all_songs()
        if len(all_songs) > 0:
            s = random.choice(all_songs)
            return songs.model.Song(s.artist, songs.model.SongTitle(s.artist, s.title), songs.model.Lyrics(s.lyrics))
        else:
            return songs.model.Song.none()


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

        return songs.model.Song(remote_song.artist, songs.model.SongTitle(remote_song.artist, remote_song.title), songs.model.Lyrics(remote_song.lyrics))
