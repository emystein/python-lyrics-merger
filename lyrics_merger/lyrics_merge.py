from lyrics_merger.song import Lyrics


class LyricsMerger(object):
    def __init__(self, lyrics_api_client, lyrics_editor):
        self.lyrics_api_client = lyrics_api_client
        self.lyrics_editor = lyrics_editor

    def merge_two_random_lyrics(self):
        song1, song2 = self.lyrics_api_client.get_random_songs(2)
        return self.lyrics_editor.interleave_lyrics(song1, song2)

    def merge_random_lyrics_by_artists(self, artist1, artist2):
        song1, song2 = self.lyrics_api_client.get_random_songs_by_artists([artist1, artist2])
        return self.lyrics_editor.interleave_lyrics(song1, song2)

    def merge_two_specific_lyrics(self, song_title1, song_title2):
        song1 = self.lyrics_api_client.get_song(song_title1)
        song2 = self.lyrics_api_client.get_song(song_title2)
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

    def __ne__(self, other):
        return self.title != other.title or self.text != other.text

    def __str__(self): 
        return self.title + '\n\n' + self.text


class EmptyMergedLyrics(MergedLyrics):
    def __init__(self):
        self.title, self.text = '', ''
