class RandomLyricsPicker:
    def pick_two(self, lyrics_library):
        return lyrics_library.get_random_songs(2)

class RandomByArtistsLyricsPicker:
    def __init__(self, artist1, artist2):
        self.artist1, self.artist2 = artist1, artist2

    def pick_two(self, lyrics_library):
        return lyrics_library.get_random_songs_by_artists([self.artist1, self.artist2])

class SpecificLyricsPicker:
    def __init__(self, song_title1, song_title2):
        self.song_title1, self.song_title2 = song_title1, song_title2

    def pick_two(self, lyrics_library):
        return lyrics_library.get_songs([self.song_title1, self.song_title2])
