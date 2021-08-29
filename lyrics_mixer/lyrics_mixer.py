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
            lyrics = self.lyrics_library.pick_using(lyrics_pickers)
            return self.lyrics_mix_strategy.mix(*lyrics)
        except Exception:
            logger.error('Returning empty lyrics.', exc_info=True)
            return MixedLyrics.empty()


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


class MixedLyrics(Lyrics):
    @staticmethod
    def with_lines(songs, lines):
        return MixedLyrics.with_paragraphs(songs, [Paragraph(lines)])
        
    @staticmethod
    def with_paragraphs(songs, paragraphs):
        song_titles = [song.title for song in songs]
        return MixedLyrics(song_titles, Paragraphs.from_list(paragraphs))

    @staticmethod
    def empty():
        return MixedLyrics([], Paragraphs.from_text(''))

    def __init__(self, song_titles, paragraphs):
        self.title = ', '.join([str(song_title) for song_title in song_titles])
        self.paragraphs = [paragraph for paragraph in paragraphs if not paragraph.is_empty()]
        self.lines = [line for paragraph in self.paragraphs for line in paragraph]
        self.text = ''.join([paragraph.text for paragraph in self.paragraphs])

    def __str__(self):
        return self.title + '\n\n' + self.text

    def has_content(self):
        return self != MixedLyrics.empty()
