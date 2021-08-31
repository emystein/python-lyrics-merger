from itertools import chain
import logging

from lyrics_mixer.lyrics_mixer import MixedLyrics

logger = logging.getLogger()


def flatten(list_of_lists):
    return list(chain(*list_of_lists))


class LineInterleaveLyricsMix:
    def mix(self, *songs):
        all_lyrics_lines = [song.lyrics.lines for song in songs]
        lines = flatten(zip(*all_lyrics_lines))
        return MixedLyrics.with_lines(songs, lines)


class ParagraphInterleaveLyricsMix:
    def mix(self, *songs):
        all_lyrics_paragraphs = [song.lyrics.paragraphs for song in songs]
        paragraphs = flatten(zip(*all_lyrics_paragraphs))
        return MixedLyrics.with_paragraphs(songs, paragraphs)


