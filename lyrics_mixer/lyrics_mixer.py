import logging
from itertools import groupby

from songs.model import Song, Lyrics

logger = logging.getLogger()


class LyricsMixer:
    def __init__(self, lyrics_library, lyrics_mix_strategy):
        self.lyrics_library = lyrics_library
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        return self.mix_lyrics(RandomSongsPicker())

    def mix_random_lyrics_by_artists(self, artist1, artist2):
        return self.mix_lyrics(RandomByArtistsSongsPicker(artist1, artist2))

    def mix_two_specific_lyrics(self, artist1, title1, artist2, title2):
        return self.mix_lyrics(SpecificSongsPicker(artist1, title1, artist2, title2))

    def mix_lyrics(self, lyrics_picker):
        try:
            song1, song2 = lyrics_picker.pick_two(self.lyrics_library)
            return self.lyrics_mix_strategy.mix(song1, song2)
        except Exception:
            logger.error('Returning empty lyrics.', exc_info=True)
            return MixedLyrics.empty()


class RandomSongsPicker:
    def pick_two(self, library):
        return library.get_random_songs(2)


class RandomByArtistsSongsPicker:
    def __init__(self, artist1, artist2):
        self.artists = [artist1, artist2]

    def pick_two(self, library):
        return library.get_random_songs_by_artists(self.artists)


class SpecificSongsPicker:
    def __init__(self, artist1, title1, artist2, title2):
        self.artist1 = artist1
        self.title1 = title1
        self.artist2 = artist2
        self.title2 = title2

    def pick_two(self, library):
        return [library.get_song(self.artist1, self.title1), library.get_song(self.artist2, self.title2)]


class LineInterleaveLyricsMix:
    def mix(self, song1, song2):
        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        lines = [val for pair in zip(
            song1.lyrics.lines(), song2.lyrics.lines()) for val in pair]
        # see https://stackoverflow.com/questions/14529523/python-split-for-lists
        paragraphs = ['\n'.join(list(l)) for k, l in groupby(
            lines, lambda x: x == '') if not k]
        return MixedLyrics(song1, song2, lines, paragraphs)


class ParagraphInterleaveLyricsMix:
    def mix(self, song1, song2):
        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        paragraphs = [val for pair in zip(
            song1.lyrics.paragraphs(), song2.lyrics.paragraphs()) for val in pair]
        lines = [lines.split('\n') for lines in paragraphs]
        # see: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        flat_list = [item for sublist in lines for item in sublist]
        return MixedLyrics(song1, song2, flat_list, paragraphs)


class MixedLyrics(Lyrics):
    @staticmethod
    def empty():
        return MixedLyrics(Song.none(), Song.none(), '', '')

    def __init__(self, song1, song2, lines, paragraphs):
        self.song1, self.song2, self.lines, self.paragraphs = song1, song2, lines, paragraphs
        self.title = f"{song1.artist} - {song1.title}, {song2.artist} - {song2.title}"
        self.text = '\n\n'.join(paragraphs)

    def __str__(self):
        return self.title + '\n\n' + self.text

    def has_content(self):
        return self != MixedLyrics.empty()
