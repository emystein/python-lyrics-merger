import logging
from lyrics_mixer.song import Lyrics


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class LyricsMixer(object):
    def __init__(self, lyrics_api_client, lyrics_mix_strategy):
        self.lyrics_api_client = lyrics_api_client
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        song1, song2 = self.lyrics_api_client.get_random_songs(2)
        return self.mix(song1, song2)

    def mix_random_lyrics_by_artists(self, artist1, artist2):
        try:
            song1, song2 = self.lyrics_api_client.get_random_songs_by_artists([artist1, artist2])
            mixed_lyrics = self.mix(song1, song2)
        except Exception as e:
            logger.error("Error mixing lyrics, returning empty lyrics", exc_info=True)
            mixed_lyrics = EmptyMixedLyrics()
        return mixed_lyrics

    def mix_two_specific_lyrics(self, song_title1, song_title2):
        song1, song2 = self.lyrics_api_client.get_songs([song_title1, song_title2])
        return self.mix(song1, song2)

    def mix(self, song1, song2):
        return self.lyrics_mix_strategy.mix_lyrics(song1, song2)


from itertools import groupby

class LineInterleaveLyricsMix(object):
    def mix_lyrics(self, song1, song2):
        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        lines = [val for pair in zip(song1.lyrics.lines(), song2.lyrics.lines()) for val in pair]
        # see https://stackoverflow.com/questions/14529523/python-split-for-lists
        paragraphs = ['\n'.join(list(l)) for k, l in groupby(lines, lambda x: x == '') if not k]
        return MixedLyrics(song1, song2, lines, paragraphs)


class ParagraphInterleaveLyricsMix(object):
    def mix_lyrics(self, song1, song2):
        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        paragraphs = [val for pair in zip(song1.lyrics.paragraphs(), song2.lyrics.paragraphs()) for val in pair]
        lines = [lines.split('\n') for lines in paragraphs]
        # see: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        flat_list = [item for sublist in lines for item in sublist]
        return MixedLyrics(song1, song2, flat_list, paragraphs)


class MixedLyrics(object):
    def __init__(self, song1, song2, lines, paragraphs):
        self.song1, self.song2, self.lines, self.paragraphs = song1, song2, lines, paragraphs
        self.title = str(song1.title) + ', ' + str(song2.title)
        self.text = '\n\n'.join(paragraphs)

    def __ne__(self, other):
        return self.title != other.title or self.text != other.text

    def __str__(self): 
        return self.title + '\n\n' + self.text


class EmptyMixedLyrics(MixedLyrics):
    def __init__(self):
        self.title, self.text = '', ''
