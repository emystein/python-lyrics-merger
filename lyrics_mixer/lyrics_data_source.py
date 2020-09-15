from azlyrics_integration.model import Artist, SongTitle, Song

class LyricsDataSource:
    """Bridge to external lyrics provider, like AZLyrics"""

    def get_song(self, title):
        return Song.entitled(title)

    def get_random_song(self):
        return self.get_song(SongTitle.random())

    def get_random_songs(self, count):
        return [self.get_random_song() for _ in range(count)]

    def get_random_songs_by_artists(self, artists):
        return [Artist.named(artist).random_song() for artist in artists]
