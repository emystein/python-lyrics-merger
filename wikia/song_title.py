import songs.model
from wikia.urls import random_song_url, song_title_from

class SongTitle:
    @staticmethod
    def random():
        return SongTitle.from_url(random_song_url())

    @staticmethod
    def from_url(url):
        artist, title = song_title_from(url)
        return songs.model.SongTitle(artist, title)
