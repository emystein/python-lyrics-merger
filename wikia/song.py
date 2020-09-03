import logging
import lyricwikia
import songs.model

logger = logging.getLogger()


class Song:
    @staticmethod
    def entitled(title):
        logger.info(f'Retrieving song: {str(title)}')

        remote_song = lyricwikia.Song(title.artist, title.title)

        return songs.model.Song(remote_song.artist, remote_song.title, remote_song.lyrics)
