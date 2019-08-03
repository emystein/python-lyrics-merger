from lyrics_merger.song import Lyrics


class LyricsMerger(object):
    def __init__(self, song_downloader, lyrics_editor):
        self.song_downloader = song_downloader
        self.lyrics_editor = lyrics_editor

    def merge_two_random_lyrics(self):
        song1 = self.song_downloader.get_random_song()
        song2 = self.song_downloader.get_random_song()
        return self.lyrics_editor.interleave_lyrics(song1, song2)

    def merge_random_lyrics_by_artists(self, artist1, artist2):
        song1 = self.song_downloader.get_random_song_by_artist(artist1)
        song2 = self.song_downloader.get_random_song_by_artist(artist2)
        return self.lyrics_editor.interleave_lyrics(song1, song2)

    def merge_two_specific_lyrics(self, song_title1, song_title2):
        song1 = self.song_downloader.get_song(song_title1)
        song2 = self.song_downloader.get_song(song_title2)
        return self.lyrics_editor.interleave_lyrics(song1, song2)


class LyricsEditor(object):
    def interleave_lyrics(self, song1, song2):
        # see: https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
        paragraphs = [val for pair in zip(song1.lyrics.paragraphs(), song2.lyrics.paragraphs()) for val in pair]
        return MergedLyrics(song1, song2, paragraphs)


class MergedLyrics(object):
    def __init__(self, song1, song2, merged_paragraphs):
        self.song1, self.song2, self.paragraphs = song1, song2, merged_paragraphs
        self.title = str(song1.title) + ', ' + str(song2.title)
        self.text = '\n\n'.join(merged_paragraphs)
