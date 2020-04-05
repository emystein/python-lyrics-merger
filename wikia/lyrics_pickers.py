class RandomLyricsPicker:
    def __init__(self, lyrics_library):
        self.lyrics_library = lyrics_library

    def pick_two(self):
        return self.lyrics_library.get_random_songs(2)


class RandomByArtistsLyricsPicker:
    def __init__(self, lyrics_library, artist1, artist2):
        self.lyrics_library, self.artist1, self.artist2 = lyrics_library, artist1, artist2

    def pick_two(self):
        return self.lyrics_library.get_random_songs_by_artists([self.artist1, self.artist2])


class SpecificLyricsPicker:
    def __init__(self, lyrics_library, song_title1, song_title2):
        self.lyrics_library, self.song_title1, self.song_title2 = lyrics_library, song_title1, song_title2

    def pick_two(self):
        return self.lyrics_library.get_songs([self.song_title1, self.song_title2])
