import logging
from songs.model import NullSong
from lyrics_mixer.mixed_lyrics import EmptyMixedLyrics


logger = logging.getLogger()


class SongPair:
    def picked_using(song_picker):
        try:
            song1, song2 = song_picker.pick_song_pair()
            return SongPair(song1, song2)
        except Exception as e:
            logger.error("Error picking songs, returning empty song pair.", exc_info=True)
            return EmptySongPair()

    def __init__(self, song1, song2):
        self.song1, self.song2 = song1, song2

    def mix_lyrics(self, lyrics_mix_strategy):
        return lyrics_mix_strategy.mix(self.song1, self.song2)


class EmptySongPair:
	def __init__(self):
		self.song1, self.song2 = NullSong(), NullSong()

	def __eq__(self, other):
		return self.song1 == other.song1 and self.song2 == other.song2
	
	def mix_lyrics(self, lyrics_mix_strategy):
		return EmptyMixedLyrics()
	
