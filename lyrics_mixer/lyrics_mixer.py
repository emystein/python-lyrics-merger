import logging
from songs.pickers import *
from songs.model import Lyrics


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
        try:
            song1, song2 = song_picker.pick_two()
            return self.lyrics_mix_strategy.mix(song1, song2)
        except Exception as e:
            logger.error("Error mixing lyrics, returning empty lyrics", exc_info=True)
            return EmptyMixedLyrics()


class MixedLyrics(object):
    def __init__(self, song1, song2, lines, paragraphs):
        self.song1, self.song2, self.lines, self.paragraphs = song1, song2, lines, paragraphs
        self.title = str(song1.title) + ', ' + str(song2.title)
        self.text = '\n\n'.join(paragraphs)

    def __eq__(self, other):
        return self.title == other.title and self.text == other.text

    def __ne__(self, other):
        return self.title != other.title or self.text != other.text

    def __str__(self): 
        return self.title + '\n\n' + self.text


class EmptyMixedLyrics(MixedLyrics):
    def __init__(self):
        self.title, self.text = '', ''
