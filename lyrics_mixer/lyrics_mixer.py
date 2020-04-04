import logging
from lyrics_mixer.lyrics_pickers import *
from lyrics_mixer.mixed_lyrics import EmptyMixedLyrics
from lyrics_mixer.mix_commands import MixCommands

logger = logging.getLogger()

class LyricsMixer(object):
    def __init__(self, lyrics_library, lyrics_mix_strategy):
        self.lyrics_library = lyrics_library
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        lyrics_picker = RandomLyricsPicker(self.lyrics_library)
        song1, song2 = lyrics_picker.pick_two_songs()
        return self.lyrics_mix_strategy.mix(song1, song2)

    def mix_random_lyrics_by_artists(self, artist1, artist2):
        lyrics_picker = RandomByArtistsLyricsPicker(self.lyrics_library, artist1, artist2)
        song1, song2 = lyrics_picker.pick_two_songs()
        return self.lyrics_mix_strategy.mix(song1, song2)

    def mix_two_specific_lyrics(self, song_title1, song_title2):
        lyrics_picker = SpecificLyricsPicker(self.lyrics_library, song_title1, song_title2)
        song1, song2 = lyrics_picker.pick_two_songs()
        return self.lyrics_mix_strategy.mix(song1, song2)

    def mix_parsed_song_titles(self, parsed_song_titles):
        mix_command = MixCommands.select_for(parsed_song_titles)
        return mix_command.mix(parsed_song_titles, self)