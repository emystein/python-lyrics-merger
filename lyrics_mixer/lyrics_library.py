from lyrics_providers.azlyrics import Artist, SongTitle, Song


class LyricsLibrary:
    """Bridge to external lyrics provider, like AZLyrics"""

    def get_song(self, artist, title):
        return Song.entitled(artist, title)

    def get_random_song(self):
        artist, title = SongTitle.random()
        return self.get_song(artist, title)

    def get_random_songs(self, count):
        return [self.get_random_song() for _ in range(count)]

    def get_random_songs_by_artists(self, artists):
        return [Artist.named(artist).random_song() for artist in artists]
