from wikia.model import Artist

class RandomLyricsPicker:
    def pick_two(self, library):
        return library.get_random_songs(2)

class RandomByArtistsLyricsPicker:
    def __init__(self, artist1, artist2):
        self.artists = [artist1, artist2]

    def pick_two(self, library):
        return library.get_random_songs_by_artists(self.artists)

class SpecificLyricsPicker:
    def __init__(self, title1, title2):
        self.titles = [title1, title2]

    def pick_two(self, library):
        return [library.get_song(title) for title in self.titles]