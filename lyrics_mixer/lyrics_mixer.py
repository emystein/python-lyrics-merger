import logging
from itertools import chain

from songs.model import Lyrics, Paragraphs, Paragraph
from lyrics_mixer.lyrics_pickers import RandomLyricsPickers, RandomByArtistLyricsPickers, \
    SpecificLyricsPickers

logger = logging.getLogger()


def flatten(list_of_lists):
    return list(chain(*list_of_lists))


class LyricsMixer:
    def __init__(self, lyrics_library, lyrics_mix_strategy):
        self.lyrics_library = lyrics_library
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        return self.mix_lyrics(RandomLyricsPickers(2))

    def mix_random_lyrics_by_artists(self, *artists):
        return self.mix_lyrics(RandomByArtistLyricsPickers(artists))

    def mix_specific_lyrics(self, *titles):
        return self.mix_lyrics(SpecificLyricsPickers(titles))

    def mix_lyrics(self, lyrics_pickers):
        try:
            lyrics = lyrics_pickers.pick_from(self.lyrics_library)
            return self.lyrics_mix_strategy.mix(*lyrics)
        except Exception:
            logger.error('Returning empty lyrics.', exc_info=True)
            return Lyrics.empty()


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


class MixedLyrics:
    @staticmethod
    def with_lines(song_titles, lines):
        return MixedLyrics.with_paragraphs(song_titles, [Paragraph(lines)])
        
    @staticmethod
    def with_paragraphs(song_titles, paragraphs):
        return Lyrics(MixedSongsTitle(song_titles), Paragraphs.from_list(paragraphs))


class MixedSongsTitle:
    def __init__(self, song_titles):
        self.artist = ', '.join([song_title.artist for song_title in song_titles])
        self.title = ', '.join([str(song_title) for song_title in song_titles])

    def is_empty(self):
        return self.title == ''

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return self.title
