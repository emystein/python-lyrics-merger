import logging
from lyrics_mixer.song_pair import SongPair, EmptySongPair


logger = logging.getLogger()


class TwoSongsPicker:
    def pick_song_pair(self):
        try:
            song1, song2 = self.pick_song_pair_internal()
            return SongPair(song1, song2)
        except Exception as e:
            logger.error("Error picking songs, returning empty song pair.", exc_info=True)
            return EmptySongPair()


class TwoRandomSongsPicker(TwoSongsPicker):
    def __init__(self, lyrics_api_client):
        self.lyrics_api_client = lyrics_api_client

    def pick_song_pair_internal(self):
        logger.info('Picking two random songs')
        return self.lyrics_api_client.get_random_songs(2)
        

class TwoRandomSongsByArtistsPicker(TwoSongsPicker):
    def __init__(self, lyrics_api_client, artist1, artist2):
        self.lyrics_api_client, self.artist1, self.artist2 = lyrics_api_client, artist1, artist2

    def pick_song_pair_internal(self):
        logger.info(f'Picking two random songs by artists: {self.artist1} and {self.artist2}')
        return self.lyrics_api_client.get_random_songs_by_artists([self.artist1, self.artist2])


class TwoSpecificSongsPicker(TwoSongsPicker):
    def __init__(self, lyrics_api_client, song_title1, song_title2):
        self.lyrics_api_client, self.song_title1, self.song_title2 = lyrics_api_client, song_title1, song_title2

    def pick_song_pair_internal(self):
        logger.info(f'Picking songs: {self.song_title1} and {self.song_title2}')
        return self.lyrics_api_client.get_songs([self.song_title1, self.song_title2])