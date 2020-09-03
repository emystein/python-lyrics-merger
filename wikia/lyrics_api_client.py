import logging
import lyricwikia
from songs.model import Song
from wikia.artist import Artist
from wikia.song_title import SongTitle


logger = logging.getLogger()


# TODO convert to module
class WikiaLyricsApiClient:
    def get_song(self, title):
        logger.info(f'Retrieving song: {str(title)}')

        remote_song = lyricwikia.Song(title.artist, title.title)

        return Song(remote_song.artist, remote_song.title, remote_song.lyrics)

    def get_random_song(self):
        return self.get_song(SongTitle.random())

    def get_random_songs(self, count):
        return [self.get_random_song() for _ in range(count)]

    # TODO: delete and use Artist directly ?
    def get_random_songs_by_artists(self, artists):
        return [Artist.named(artist).random_song() for artist in artists]
