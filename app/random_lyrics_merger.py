from app.lyrics import Lyrics


class MergedLyrics(object):
    def __init__(self, song1, song2, merged_paragraphs):
        self.song1 = song1
        self.song2 = song2
        self.title = str(song1.title) + ', ' + str(song2.title)
        self.paragraphs = merged_paragraphs
        self.text = '\n\n'.join(merged_paragraphs)


class RandomLyricsMerger(object):
    def __init__(self, downloader, lyrics_editor):
        self.downloader = downloader
        self.lyrics_editor = lyrics_editor

    def merge_two_random_lyrics(self):
        song1 = self.downloader.get_random()
        song2 = self.downloader.get_random()
        return self.lyrics_editor.merge(song1, song2)
