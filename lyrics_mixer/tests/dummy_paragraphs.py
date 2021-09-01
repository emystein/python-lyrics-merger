from songs.model import Paragraph, Line


class DummyParagraphs:
    @staticmethod
    def for_lyrics(lyrics_number):
        return DummyParagraphsBuilder(lyrics_number)


class DummyParagraphsBuilder:
    def __init__(self, lyrics_number):
        self.lyrics_number = lyrics_number

    def with_paragraphs(self, paragraph_count):
        return DummyParagraphBuilder(self.lyrics_number, paragraph_count)


class DummyParagraphBuilder:
    def __init__(self, lyrics_number, paragraph_count):
        self.lyrics_number = lyrics_number
        self.paragraph_count = paragraph_count

    def each_with_lines(self, number_of_lines):
        paragraphs = []

        for paragraph_number in range(1, self.paragraph_count + 1):
            lines = [self.line(paragraph_number, line_number) for line_number in range(1, number_of_lines + 1)]
            paragraphs.append(Paragraph(lines))

        return paragraphs

    def line(self, paragraph_number, line_number):
        return Line(f"lyrics {self.lyrics_number}, paragraph {paragraph_number}, line {line_number}")


