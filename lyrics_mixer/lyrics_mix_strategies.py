from itertools import groupby
from lyrics_mixer.mixed_lyrics import MixedLyrics

class LineInterleaveLyricsMix(object):
    def mix(self, song1, song2):
        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        lines = [val for pair in zip(song1.lyrics.lines(), song2.lyrics.lines()) for val in pair]
        # see https://stackoverflow.com/questions/14529523/python-split-for-lists
        paragraphs = ['\n'.join(list(l)) for k, l in groupby(lines, lambda x: x == '') if not k]
        return MixedLyrics(song1, song2, lines, paragraphs)


class ParagraphInterleaveLyricsMix(object):
    def mix(self, song1, song2):
        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        paragraphs = [val for pair in zip(song1.lyrics.paragraphs(), song2.lyrics.paragraphs()) for val in pair]
        lines = [lines.split('\n') for lines in paragraphs]
        # see: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        flat_list = [item for sublist in lines for item in sublist]
        return MixedLyrics(song1, song2, flat_list, paragraphs)