import logging


logger = logging.getLogger()


class TwoSongsPicker:
    def __init__(self, lyrics_api_client):
        self.lyrics_api_client = lyrics_api_client


class TwoRandomSongsPicker(TwoSongsPicker):
    def pick_two_songs(self):
        logger.info('Mixing two random lyrics')
        return self.lyrics_api_client.get_random_songs(2)
        

class TwoRandomSongsByArtistsPicker(TwoSongsPicker):
    def __init__(self, lyrics_api_client, artist1, artist2):
        self.lyrics_api_client = lyrics_api_client
        self.artist1, self.artist2 = artist1, artist2

    def pick_two_songs(self):
        return self.lyrics_api_client.get_random_songs_by_artists([self.artist1, self.artist2])


class TwoSpecificSongsPicker(TwoSongsPicker):
    def __init__(self, lyrics_api_client, song_title1, song_title2):
        self.lyrics_api_client = lyrics_api_client
        self.song_title1, self.song_title2 = song_title1, song_title2

    def pick_two_songs(self):
        return self.lyrics_api_client.get_songs([self.song_title1, self.song_title2])