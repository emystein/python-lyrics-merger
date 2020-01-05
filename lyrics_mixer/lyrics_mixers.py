from lyrics_mixer.mixed_lyrics import EmptyMixedLyrics
from songs.model import NullSong
import logging


logger = logging.getLogger()


class LyricsMixer:
    def mix_lyrics(self, lyrics_mix_strategy):
        try:
            song1, song2 = self.pick_two_songs()
            return lyrics_mix_strategy.mix(song1, song2)
        except Exception as e:
            logger.error('Error picking songs, returning empty lyrics.', exc_info=True)
            return EmptyMixedLyrics()


class RandomLyricsMixer(LyricsMixer):
    def __init__(self, lyrics_api_client):
        self.lyrics_api_client = lyrics_api_client

    def pick_two_songs(self):
        return self.lyrics_api_client.get_random_songs(2)


class RandomByArtistsLyricsMixer(LyricsMixer):
    def __init__(self, lyrics_api_client, artist1, artist2):
        self.lyrics_api_client, self.artist1, self.artist2 = lyrics_api_client, artist1, artist2

    def pick_two_songs(self):
        return self.lyrics_api_client.get_random_songs_by_artists([self.artist1, self.artist2])


class SpecificLyricsMixer(LyricsMixer):
    def __init__(self, lyrics_api_client, song_title1, song_title2):
        self.lyrics_api_client, self.song_title1, self.song_title2 = lyrics_api_client, song_title1, song_title2

    def pick_two_songs(self):
        return self.lyrics_api_client.get_songs([self.song_title1, self.song_title2])
