import logging
from lyrics_mixer.lyrics_mixers import *


class Dispatcher(object):
    def __init__(self, lyrics_library, lyrics_mix_strategy):
        self.lyrics_library = lyrics_library
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        lyrics_mixer = RandomLyricsMixer(self.lyrics_library)
        return lyrics_mixer.mix_lyrics(self.lyrics_mix_strategy)

    def mix_random_lyrics_by_artists(self, artist1, artist2):
        lyrics_mixer = RandomByArtistsLyricsMixer(self.lyrics_library, artist1, artist2)
        return lyrics_mixer.mix_lyrics(self.lyrics_mix_strategy)

    def mix_two_specific_lyrics(self, song_title1, song_title2):
        lyrics_mixer = SpecificLyricsMixer(self.lyrics_library, song_title1, song_title2)
        return lyrics_mixer.mix_lyrics(self.lyrics_mix_strategy)
