from azlyrics_wrapper.model import Artist, SongTitle, Song


class LyricsDataSource:
    def get_song(self, title):
        return Song.entitled(title)

    def get_random_song(self):
        return self.get_song(SongTitle.random())

    def get_random_songs(self, count):
        return [self.get_random_song() for _ in range(count)]

    def get_random_songs_by_artists(self, artists):
        return [Artist.named(artist).random_song() for artist in artists]


class RandomSongsPicker:
    def pick_two(self, library):
        return library.get_random_songs(2)


class RandomByArtistsSongsPicker:
    def __init__(self, artist1, artist2):
        self.artists = [artist1, artist2]

    def pick_two(self, library):
        return library.get_random_songs_by_artists(self.artists)


class SpecificSongsPicker:
    def __init__(self, title1, title2):
        self.titles = [title1, title2]

    def pick_two(self, library):
        return [library.get_song(title) for title in self.titles]

