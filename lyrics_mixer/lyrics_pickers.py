class LyricsPickers:
    def pick_from(self, library):
        return [picker.pick_from(library) for picker in self.pickers]


class RandomLyricsPickers(LyricsPickers):
    def __init__(self, count):
        self.pickers = [RandomLyricsPicker() for _ in range(count)]


class RandomLyricsPicker:
    def pick_from(self, library):
        return library.get_random_lyrics()


class RandomByArtistLyricsPickers(LyricsPickers):
    def __init__(self, artists):
        self.pickers = [RandomByArtistLyricsPicker(artist) for artist in artists]


class RandomByArtistLyricsPicker:
    def __init__(self, artist):
        self.artist = artist

    def pick_from(self, library):
        return library.get_random_lyrics_by_artist(self.artist)


class SpecificLyricsPickers(LyricsPickers):
    def __init__(self, titles):
        self.pickers = [SpecificLyricsPicker(title) for title in titles]


class SpecificLyricsPicker:
    def __init__(self, title):
        self.title = title

    def pick_from(self, library):
        return library.get_lyrics(self.title)
