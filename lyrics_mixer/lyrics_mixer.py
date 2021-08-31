import logging

from lyrics_mixer.lyrics_pickers import *
from lyrics_mixer.mixed_lyrics import MixedLyrics
from songs.model import Lyrics

logger = logging.getLogger()


class LyricsMixer:
    def __init__(self, lyrics_library, lyrics_mix_strategy):
        self.lyrics_library = lyrics_library
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        return self.mix_lyrics(RandomLyricsPickers(2))

    def mix_random_lyrics_by_artists(self, *artists):
        return self.mix_lyrics(RandomByArtistLyricsPickers(artists))

    def mix_specific_lyrics(self, *titles):
        return self.mix_lyrics(SpecificLyricsPickers(titles))

    def mix_lyrics(self, lyrics_pickers):
        try:
            lyrics = lyrics_pickers.pick_from(self.lyrics_library)
            return self.lyrics_mix_strategy.mix(*lyrics)
        except Exception:
            logger.error('Returning empty lyrics.', exc_info=True)
            return Lyrics.empty()
