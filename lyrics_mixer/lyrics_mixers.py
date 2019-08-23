from lyrics_mixer.mixed_lyrics import EmptyMixedLyrics
from songs.model import NullSong
import logging


logger = logging.getLogger()


class LyricsMixer:
    def mix_lyrics(self):
        try:
            song1, song2 = self.pick_song_pair_internal()
            song_pair = SongPair(song1, song2)
            return song_pair.mix_lyrics(self.lyrics_mix_strategy)
        except Exception as e:
            logger.error('Error picking songs, returning empty lyrics.', exc_info=True)
            return EmptyMixedLyrics()


class RandomLyricsMixer(LyricsMixer):
    def __init__(self, lyrics_api_client, lyrics_mix_strategy):
        self.lyrics_api_client = lyrics_api_client
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def pick_song_pair_internal(self):
        return self.lyrics_api_client.get_random_songs(2)


class RandomByArtistsLyricsMixer(LyricsMixer):
    def __init__(self, lyrics_api_client, lyrics_mix_strategy, artist1, artist2):
        self.lyrics_api_client, self.lyrics_mix_strategy, self.artist1, self.artist2 = lyrics_api_client, lyrics_mix_strategy, artist1, artist2

    def pick_song_pair_internal(self):
        return self.lyrics_api_client.get_random_songs_by_artists([self.artist1, self.artist2])


class SpecificLyricsMixer(LyricsMixer):
    def __init__(self, lyrics_api_client, lyrics_mix_strategy, song_title1, song_title2):
        self.lyrics_api_client, self.lyrics_mix_strategy, self.song_title1, self.song_title2 = lyrics_api_client, lyrics_mix_strategy, song_title1, song_title2

    def pick_song_pair_internal(self):
        return self.lyrics_api_client.get_songs([self.song_title1, self.song_title2])


class SongPair:
    def __init__(self, song1, song2):
        self.song1, self.song2 = song1, song2

    def __eq__(self, other):
        return self.song1 == other.song1 and self.song2 == other.song2

    def mix_lyrics(self, lyrics_mix_strategy):
        return lyrics_mix_strategy.mix(self.song1, self.song2)


class EmptySongPair:
    def __init__(self):
        self.song1, self.song2 = NullSong(), NullSong()

    def __eq__(self, other):
        return other.song1 == other.song2 == NullSong()

    def mix_lyrics(self, lyrics_mix_strategy):
        return EmptyMixedLyrics()
