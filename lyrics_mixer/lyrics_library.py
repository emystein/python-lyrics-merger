from lyrics_providers.azlyrics import Artist, SongTitle, Song


class LyricsLibrary:
    """Bridge to external lyrics provider, like AZLyrics"""

    def get_lyrics(self, artist, title):
        return Song.entitled(artist, title)

    def get_random_lyrics(self, count):
        return [self.get_single_random_lyrics() for _ in range(count)]

    def get_random_lyrics_by_artists(self, artists):
        return [Artist.named(artist).random_song() for artist in artists]

    def __get_single_random_lyrics__(self):
        artist, title = SongTitle.random()
        return self.get_lyrics(artist, title)
