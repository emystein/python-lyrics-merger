import logging
from lyrics_mixer.lyrics_pickers import *
from lyrics_mixer.mixed_lyrics import EmptyMixedLyrics

logger = logging.getLogger()

class LyricsMixer(object):
    def __init__(self, lyrics_library, lyrics_mix_strategy):
        self.lyrics_library = lyrics_library
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        lyrics_mixer = RandomLyricsPicker(self.lyrics_library)
        try:
            song1, song2 = lyrics_mixer.pick_two_songs()
        except Exception as e:
            logger.error('Error picking songs, returning empty lyrics.', exc_info=True)
            return EmptyMixedLyrics()
        return self.lyrics_mix_strategy.mix(song1, song2)

    def mix_random_lyrics_by_artists(self, artist1, artist2):
        lyrics_mixer = RandomByArtistsLyricsPicker(self.lyrics_library, artist1, artist2)
        try:
            song1, song2 = lyrics_mixer.pick_two_songs()
        except Exception as e:
            logger.error('Error picking songs, returning empty lyrics.', exc_info=True)
            return EmptyMixedLyrics()
        return self.lyrics_mix_strategy.mix(song1, song2)

    def mix_two_specific_lyrics(self, song_title1, song_title2):
        lyrics_mixer = SpecificLyricsPicker(self.lyrics_library, song_title1, song_title2)
        try:
            song1, song2 = lyrics_mixer.pick_two_songs()
        except Exception as e:
            logger.error('Error picking songs, returning empty lyrics.', exc_info=True)
            return EmptyMixedLyrics()
        return self.lyrics_mix_strategy.mix(song1, song2)