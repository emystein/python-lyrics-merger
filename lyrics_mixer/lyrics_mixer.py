import logging
from itertools import groupby

from songs.model import Lyrics
from lyrics_mixer.lyrics_pickers import RandomLyricsPickers, RandomByArtistLyricsPickers, \
    SpecificLyricsPickers

logger = logging.getLogger()


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
        all_lyrics_lines = [song.lyrics.lines() for song in songs]

        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        lines = [val for pair in zip(*all_lyrics_lines) for val in pair]
        # see https://stackoverflow.com/questions/14529523/python-split-for-lists
        paragraphs = ['\n'.join(list(l)) for k, l in groupby(lines, lambda x: x == '') if not k]

        return MixedLyrics.all(songs, paragraphs)


class ParagraphInterleaveLyricsMix:
    def mix(self, *songs):
        all_lyrics_paragraphs = [song.lyrics.paragraphs() for song in songs]

        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        paragraphs = [val for pair in zip(*all_lyrics_paragraphs) for val in pair]
        lines = [lines.split('\n') for lines in paragraphs]
        # see: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        flat_list = [item for sublist in lines for item in sublist]

        return MixedLyrics.all(songs, paragraphs)


class MixedLyrics(Lyrics):
    @staticmethod
    def all(songs, paragraphs):
        song_titles = [song.title for song in songs]
        return MixedLyrics(song_titles, paragraphs)

    @staticmethod
    def empty():
        return MixedLyrics([], [])

    def __init__(self, song_titles, paragraphs):
        self.paragraphs = paragraphs
        lines = []
        for paragraph in paragraphs:
            paragraph_lines = paragraph.splitlines()
            for paragraph_line in paragraph_lines:
                lines.append(paragraph_line)
        self.lines = lines
        self.title = ', '.join([str(song_title) for song_title in song_titles])
        self.text = '\n\n'.join(paragraphs)

    def __str__(self):
        return self.title + '\n\n' + self.text

    def has_content(self):
        return self != MixedLyrics.empty()
