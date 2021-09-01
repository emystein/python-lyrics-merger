import logging
from lyrics_mixer.lists import flatten
from lyrics_mixer.lyrics_mixer import MixedLyrics

logger = logging.getLogger()


class LineInterleaveLyricsMix:
    def mix(self, *lyrics):
        all_lyrics_lines = [lyric.lines for lyric in lyrics]
        lines = flatten(zip(*all_lyrics_lines))
        song_titles = [lyric.title for lyric in lyrics]
        return MixedLyrics.with_lines(song_titles, lines)


class ParagraphInterleaveLyricsMix:
    def mix(self, *lyrics):
        all_lyrics_paragraphs = [lyric.paragraphs for lyric in lyrics]
        paragraphs = flatten(zip(*all_lyrics_paragraphs))
        song_titles = [lyric.title for lyric in lyrics]
        return MixedLyrics.with_paragraphs(song_titles, paragraphs)



