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
    def __init__(self, lyrics_library):
        self.lyrics_library = lyrics_library

    def pick_two_songs(self):
        return self.lyrics_library.get_random_songs(2)


class RandomByArtistsLyricsMixer(LyricsMixer):
    def __init__(self, lyrics_library, artist1, artist2):
        self.lyrics_library, self.artist1, self.artist2 = lyrics_library, artist1, artist2

    def pick_two_songs(self):
        return self.lyrics_library.get_random_songs_by_artists([self.artist1, self.artist2])


class SpecificLyricsMixer(LyricsMixer):
    def __init__(self, lyrics_library, song_title1, song_title2):
        self.lyrics_library, self.song_title1, self.song_title2 = lyrics_library, song_title1, song_title2

    def pick_two_songs(self):
        return self.lyrics_library.get_songs([self.song_title1, self.song_title2])
