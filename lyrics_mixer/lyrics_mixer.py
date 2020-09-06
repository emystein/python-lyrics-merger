import logging
from wikia.lyrics_pickers import *
from itertools import groupby
from lyrics_mixer.song_titles_parser import ParsedSongTitles, ParsedArtists


logger = logging.getLogger()


class LyricsMixer:
    def __init__(self, lyrics_library, lyrics_mix_strategy):
        self.lyrics_library = lyrics_library
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        return self.mix_lyrics(RandomLyricsPicker())

    def mix_random_lyrics_by_artists(self, artist1, artist2):
        return self.mix_lyrics(RandomByArtistsLyricsPicker(artist1, artist2))

    def mix_two_specific_lyrics(self, song_title1, song_title2):
        return self.mix_lyrics(SpecificLyricsPicker(song_title1, song_title2))

    def mix_lyrics(self, lyrics_picker):
        try:
            song1, song2 = lyrics_picker.pick_two(self.lyrics_library)
            return self.lyrics_mix_strategy.mix(song1, song2)
        except Exception as e:
            logger.error('Returning empty lyrics.', exc_info=True)
            return EmptyMixedLyrics()


class LineInterleaveLyricsMixStrategy:
    def mix(self, song1, song2):
        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        lines = [val for pair in zip(
            song1.lyrics.lines(), song2.lyrics.lines()) for val in pair]
        # see https://stackoverflow.com/questions/14529523/python-split-for-lists
        paragraphs = ['\n'.join(list(l)) for k, l in groupby(
            lines, lambda x: x == '') if not k]
        return MixedLyrics(song1, song2, lines, paragraphs)


class ParagraphInterleaveLyricsMixStrategy:
    def mix(self, song1, song2):
        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        paragraphs = [val for pair in zip(
            song1.lyrics.paragraphs(), song2.lyrics.paragraphs()) for val in pair]
        lines = [lines.split('\n') for lines in paragraphs]
        # see: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        flat_list = [item for sublist in lines for item in sublist]
        return MixedLyrics(song1, song2, flat_list, paragraphs)


class MixedLyrics:
    def __init__(self, song1, song2, lines, paragraphs):
        self.song1, self.song2, self.lines, self.paragraphs = song1, song2, lines, paragraphs
        self.title = str(song1.title) + ', ' + str(song2.title)
        self.text = '\n\n'.join(paragraphs)

    def __eq__(self, other):
        return self.title == other.title and self.text == other.text

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.title + '\n\n' + self.text


class EmptyMixedLyrics(MixedLyrics):
    def __init__(self):
        self.title, self.text = '', ''
