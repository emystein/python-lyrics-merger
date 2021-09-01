from songs.model import Paragraph, Line


class DummyParagraphs:
    @staticmethod
    def chapter(chapter):
        return DummyParagraphsBuilder(chapter)


class DummyParagraphsBuilder:
    def __init__(self, chapter):
        self.chapter = chapter

    def count(self, paragraph_count):
        return DummyParagraphBuilder(self.chapter, paragraph_count)


class DummyParagraphBuilder:
    def __init__(self, chapter, paragraph_count):
        self.chapter = chapter
        self.paragraph_count = paragraph_count

    def lines_per_each(self, number_of_lines):
        paragraphs = []

        for paragraph_number in range(1, self.paragraph_count + 1):
            lines = [self.line(paragraph_number, line_number) for line_number in range(1, number_of_lines + 1)]
            paragraphs.append(Paragraph(lines))

        return paragraphs

    def line(self, paragraph_number, line_number):
        return Line(f"chapter {self.chapter}, paragraph {paragraph_number}, line {line_number}")


