import logging
from lyrics_mixer.lyrics_pickers import *
from itertools import groupby
from lyrics_mixer.song_titles_parser import ParsedSongTitles, ParsedArtists


logger = logging.getLogger()


class LyricsMixer:
    def __init__(self, lyrics_library, lyrics_mix_strategy):
        self.lyrics_library = lyrics_library
        self.lyrics_mix_strategy = lyrics_mix_strategy

    def mix_two_random_lyrics(self):
        lyrics_picker = RandomLyricsPicker(self.lyrics_library)
        return self.pick_and_mix_two_lyrics(lyrics_picker)

    def mix_random_lyrics_by_artists(self, artist1, artist2):
        lyrics_picker = RandomByArtistsLyricsPicker(self.lyrics_library, artist1, artist2)
        return self.pick_and_mix_two_lyrics(lyrics_picker)

    def mix_two_specific_lyrics(self, song_title1, song_title2):
        lyrics_picker = SpecificLyricsPicker(self.lyrics_library, song_title1, song_title2)
        return self.pick_and_mix_two_lyrics(lyrics_picker)

    def pick_and_mix_two_lyrics(self, lyrics_picker):
        song1, song2 = lyrics_picker.pick_two()
        return self.lyrics_mix_strategy.mix(song1, song2)

    def mix_parsed_song_titles(self, parsed_song_titles):
        mix_command = MixCommands.select_for(parsed_song_titles)

        try:
            return mix_command.mix(parsed_song_titles, self)
        except Exception as e:
            logger.error('Returning empty lyrics.', exc_info=True)
            return EmptyMixedLyrics()


class MixCommands:
    @staticmethod
    def select_for(parsed):
        mix_commands = [ArtistsMixCommand(), SongTitlesMixCommand()]

        return next(mix_command for mix_command in mix_commands if mix_command.accepts(parsed))


class ArtistsMixCommand:
    def accepts(self, parsed):
        return isinstance(parsed, ParsedArtists)

    def mix(self, parsed, lyrics_mixer):
        return lyrics_mixer.mix_random_lyrics_by_artists(parsed.song_title1.artist, parsed.song_title2.artist)


class SongTitlesMixCommand:
    def accepts(self, parsed):
        return isinstance(parsed, ParsedSongTitles)

    def mix(self, parsed, lyrics_mixer):
        return lyrics_mixer.mix_two_specific_lyrics(parsed.song_title1, parsed.song_title2)


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
