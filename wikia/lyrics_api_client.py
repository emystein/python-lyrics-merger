import logging
import lyricwikia
import random
from songs.model import Song, NullSong
from wikia.song_title import random_song_title


logger = logging.getLogger()


# TODO convert to module
class WikiaLyricsApiClient:
    def get_song(self, song_title):
        logger.info(f'Retrieving song: {str(song_title)}')

        remote_song = lyricwikia.Song(song_title.artist, song_title.title)

        return Song(remote_song.artist, remote_song.title, remote_song.lyrics)

    def get_songs(self, song_titles):
        return [self.get_song(title) for title in song_titles]

    def get_random_song(self):
        logger.info('Retrieving random song')

        return self.get_song(random_song_title())

    def get_random_songs(self, count):
        return [self.get_random_song() for _ in range(count)]

    def get_random_song_by_artist(self, artist):
        logger.info(f'Retrieving random song by artist: {artist}')

        remote_songs = self.find_all_songs_by_artist(artist)

        if len(remote_songs) > 0:
            remote_song = random.choice(remote_songs)
            return Song(remote_song.artist, remote_song.title, remote_song.lyrics)
        else:
            return NullSong()

    def get_random_songs_by_artists(self, artists):
        return [self.get_random_song_by_artist(artist) for artist in artists]

    def find_all_songs_by_artist(self, artist_name):
        artist = lyricwikia.Artist(artist_name)

        songs = []

        for album in artist.albums:
            songs.extend(album.songs)

        return songs
