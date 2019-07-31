from app.lyrics import Lyrics


class RandomLyricsMerger(object):
    def __init__(self, lyrics_downloader, lyrics_editor):
        self.lyrics_downloader = lyrics_downloader
        self.lyrics_editor = lyrics_editor

    def merge_two_random_lyrics(self):
        song1 = self.lyrics_downloader.get_random()
        song2 = self.lyrics_downloader.get_random()
        return self.lyrics_editor.merge(song1, song2)


class LyricsEditor(object):
    def merge(self, song1, song2):
        lyrics1 = Lyrics(song1.lyrics)
        lyrics2 = Lyrics(song2.lyrics)
        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        paragraphs = [val for pair in zip(lyrics1.paragraphs(), lyrics2.paragraphs()) for val in pair]
        return MergedLyrics(song1, song2, paragraphs)


class MergedLyrics(object):
    def __init__(self, song1, song2, merged_paragraphs):
        self.song1 = song1
        self.song2 = song2
        self.title = str(song1.title) + ', ' + str(song2.title)
        self.paragraphs = merged_paragraphs
        self.text = '\n\n'.join(merged_paragraphs)
