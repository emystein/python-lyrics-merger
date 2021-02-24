import logging
from itertools import groupby

from songs.model import SongTitle, Song, Lyrics

logger = logging.getLogger()


class LyricsMixer:
    def __init__(self, lyrics_library, lyrics_mix_strategy):
        self.lyrics_library = lyrics_library
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        return self.mix_lyrics(ManyRandomLyricsPickers(2))

    def mix_random_lyrics_by_artists(self, *artists):
        return self.mix_lyrics(ManyRandomByArtistLyricsPickers(artists))

    def mix_specific_lyrics(self, *titles):
        return self.mix_lyrics(ManySpecificLyricsPickers(titles))

    def mix_lyrics(self, lyrics_pickers):
        try:
            lyrics = [picker.pick(self.lyrics_library) for picker in lyrics_pickers.pickers]
            return self.lyrics_mix_strategy.mix(*lyrics)
        except Exception:
            logger.error('Returning empty lyrics.', exc_info=True)
            return MixedLyrics.empty()

class RandomLyricsPicker:
    def pick(self, library):
        return library.get_random_lyrics()


class RandomByArtistLyricsPicker:
    def __init__(self, artist):
        self.artist = artist

    def pick(self, library):
        return library.get_random_lyrics_by_artist(self.artist)


class SpecificLyricsPicker:
    def __init__(self, title):
        self.title = title

    def pick(self, library):
        return library.get_lyrics(self.title.artist, self.title.title)


class ManyRandomLyricsPickers:
    def __init__(self, count):
        self.pickers = [RandomLyricsPicker() for number in range(count)]


class ManyRandomByArtistLyricsPickers:
    def __init__(self, artists):
        self.pickers = [RandomByArtistLyricsPicker(artist) for artist in artists]


class ManySpecificLyricsPickers:
    def __init__(self, titles):
        self.pickers = [SpecificLyricsPicker(title) for title in titles]


class LineInterleaveLyricsMix:
    def mix(self, *songs):
        all_lyrics_lines = map(lambda song: song.lyrics.lines(), songs)

        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        lines = [val for pair in zip(*all_lyrics_lines) for val in pair]
        # see https://stackoverflow.com/questions/14529523/python-split-for-lists
        paragraphs = ['\n'.join(list(l)) for k, l in groupby(
            lines, lambda x: x == '') if not k]

        return MixedLyrics.all(songs, lines, paragraphs)


class ParagraphInterleaveLyricsMix:
    def mix(self, *songs):
        all_lyrics_paragraphs = map(lambda song: song.lyrics.paragraphs(), songs)

        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        paragraphs = [val for pair in zip(*all_lyrics_paragraphs) for val in pair]
        lines = [lines.split('\n') for lines in paragraphs]
        # see: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        flat_list = [item for sublist in lines for item in sublist]

        return MixedLyrics.all(songs, flat_list, paragraphs)


class MixedLyrics(Lyrics):
    @staticmethod
    def all(songs, lines, paragraphs):
        return MixedLyrics(songs[0], songs[1], lines, paragraphs)

    @staticmethod
    def empty():
        return MixedLyrics(Song.none(), Song.none(), '', '')

    def __init__(self, song1, song2, lines, paragraphs):
        self.song1, self.song2, self.lines, self.paragraphs = song1, song2, lines, paragraphs
        self.songs = [self.song1, self.song2]
        self.artist1 = self.song1.artist
        self.artist2 = self.song2.artist
        self.title = f"{song1.artist} - {song1.title}, {song2.artist} - {song2.title}"
        self.text = '\n\n'.join(paragraphs)

    def __str__(self):
        return self.title + '\n\n' + self.text

    def has_content(self):
        return self != MixedLyrics.empty()
