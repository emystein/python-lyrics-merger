from lyrics_providers.azlyrics import Artist, SongTitle, Song


class LyricsLibrary:
    """Bridge to external lyrics provider, like AZLyrics"""

    def get_lyrics(self, title):
        return Song.entitled(title)

    def get_random_lyrics(self):
        return self.get_lyrics(SongTitle.random())
        
    def get_random_lyrics_by_artist(self, artist):
        return Artist.named(artist).random_song()

    def pick_using(self, lyrics_pickers):
        return lyrics_pickers.pick_from(self)
