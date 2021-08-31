from songs.model import Lyrics, Paragraphs, Paragraph


class MixedLyrics:
    @staticmethod
    def with_lines(songs, lines):
        return MixedLyrics.with_paragraphs(songs, [Paragraph(lines)])

    @staticmethod
    def with_paragraphs(songs, paragraphs):
        return Lyrics(MixedSongsTitle(songs), Paragraphs.from_list(paragraphs))

    @staticmethod
    def empty():
        return Lyrics(MixedSongsTitle([]), Paragraphs.from_text(''))


class MixedSongsTitle:
    def __init__(self, songs):
        song_titles = [song.title for song in songs]
        self.artist = ', '.join([song_title.artist for song_title in song_titles])
        self.title = ', '.join([str(song_title) for song_title in song_titles])

    def is_empty(self):
        return self.title == ''

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return self.title
