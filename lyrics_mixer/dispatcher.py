import logging
from lyrics_mixer.lyrics_mixers import *


class Dispatcher(object):
    def __init__(self, lyrics_api_client, lyrics_mix_strategy):
        self.lyrics_api_client = lyrics_api_client
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        lyrics_mixer = RandomLyricsMixer(self.lyrics_api_client, self.lyrics_mix_strategy)
        return lyrics_mixer.mix_lyrics()

    def mix_random_lyrics_by_artists(self, artist1, artist2):
        lyrics_mixer = RandomByArtistsLyricsMixer(self.lyrics_api_client, self.lyrics_mix_strategy, artist1, artist2)
        return lyrics_mixer.mix_lyrics()

    def mix_two_specific_lyrics(self, song_title1, song_title2):
        lyrics_mixer = SpecificLyricsMixer(self.lyrics_api_client, self.lyrics_mix_strategy, song_title1, song_title2)
        return lyrics_mixer.mix_lyrics()

