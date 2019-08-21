class MixedLyrics:
    def __init__(self, song1, song2, lines, paragraphs):
        self.song1, self.song2, self.lines, self.paragraphs = song1, song2, lines, paragraphs
        self.title = str(song1.title) + ', ' + str(song2.title)
        self.text = '\n\n'.join(paragraphs)

    def __eq__(self, other):
        return self.title == other.title and self.text == other.text

    def __ne__(self, other):
        return self.title != other.title or self.text != other.text

    def __str__(self):
        return self.title + '\n\n' + self.text


class EmptyMixedLyrics(MixedLyrics):
    def __init__(self):
        self.title, self.text = '', ''