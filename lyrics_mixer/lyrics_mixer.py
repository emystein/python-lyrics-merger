import logging
from lyrics_mixer.pickers import *
from songs.model import Lyrics, NullSong
from lyrics_mixer.song_pair import SongPair


logger = logging.getLogger()


class LyricsMixer(object):
    def __init__(self, lyrics_api_client, lyrics_mix_strategy):
        self.lyrics_api_client = lyrics_api_client
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        song_picker = TwoRandomSongsPicker(self.lyrics_api_client)
        return self.mix_using_picker(song_picker)

    def mix_random_lyrics_by_artists(self, artist1, artist2):
        song_picker = TwoRandomSongsByArtistsPicker(self.lyrics_api_client, artist1, artist2)
        return self.mix_using_picker(song_picker)

    def mix_two_specific_lyrics(self, song_title1, song_title2):
        song_picker = TwoSpecificSongsPicker(self.lyrics_api_client, song_title1, song_title2)
        return self.mix_using_picker(song_picker)

    def mix_using_picker(self, song_picker):
        songs = song_picker.pick_song_pair()
        return songs.mix_lyrics(self.lyrics_mix_strategy)

