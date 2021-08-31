from songs.model import Lyrics, Paragraphs, Paragraph


class MixedLyrics:
    @staticmethod
    def with_lines(song_titles, lines):
        return MixedLyrics.with_paragraphs(song_titles, [Paragraph(lines)])

    @staticmethod
    def with_paragraphs(song_titles, paragraphs):
        return Lyrics(MixedSongsTitle(song_titles), Paragraphs.from_list(paragraphs))


class MixedSongsTitle:
    def __init__(self, song_titles):
        self.artist = ', '.join([song_title.artist for song_title in song_titles])
        self.title = ', '.join([str(song_title) for song_title in song_titles])

    def is_empty(self):
        return self.title == ''

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return self.title
