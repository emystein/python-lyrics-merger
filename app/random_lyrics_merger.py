from app.lyrics import Lyrics


class MergedLyrics(object):
    def __init__(self, song1, song2, merged_text):
        self.song1 = song1
        self.song2 = song2
        self.title = str(song1.title) + ', ' + str(song2.title)
        self.merged_text = merged_text


class RandomLyricsMerger(object):
    def __init__(self, downloader, lyrics_editor):
        self.downloader = downloader
        self.lyrics_editor = lyrics_editor

    def merge_two_random_lyrics(self):
        song1 = self.downloader.get_random()
        lyrics1 = Lyrics(song1.lyrics)
        song2 = self.downloader.get_random()
        lyrics2 = Lyrics(song2.lyrics)
        merged_paragraphs = self.lyrics_editor.merge(lyrics1, lyrics2)
        merged_text = '\n\n'.join(merged_paragraphs)
        # TODO make lyrics_editor to return MergedLyrics
        return MergedLyrics(song1, song2, merged_text)
