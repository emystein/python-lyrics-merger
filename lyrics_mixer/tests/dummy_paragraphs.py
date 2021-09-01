from songs.model import Paragraph, Line


class DummyChapter:
    @staticmethod
    def number(chapter):
        return DummyChapterBuilder(chapter)


class DummyChapterBuilder:
    def __init__(self, chapter):
        self.chapter = chapter

    def paragraph_count(self, paragraph_count):
        return DummyParagraphBuilder(self.chapter, paragraph_count)


class DummyParagraphBuilder:
    def __init__(self, chapter, paragraph_count):
        self.chapter = chapter
        self.paragraph_numbers = range(1, paragraph_count + 1)

    def lines_per_paragraph(self, number_of_lines):
        return [Paragraph(self.lines(paragraph_number, number_of_lines))
                for paragraph_number in self.paragraph_numbers]

    def lines(self, paragraph_number, number_of_lines):
        line_numbers = range(1, number_of_lines + 1)
        return [self.line(paragraph_number, line_number) for line_number in line_numbers]

    def line(self, paragraph_number, line_number):
        return Line(f"chapter {self.chapter}, paragraph {paragraph_number}, line {line_number}")
