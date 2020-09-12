from wikia.lyrics import WikiaLyrics
from wikia.model import Artist

class LyricsDataSource:
    def __init__(self):
      self.data_source = WikiaLyrics()

    def get_song(self, title):
        return self.data_source.get_song(title)

    def get_random_song(self):
        return self.data_source.get_random_song()

    def get_random_songs(self, count):
        return self.data_source.get_random_songs(count)

    def get_random_songs_by_artists(self, artists):
        return self.data_source.get_random_songs_by_artists(artists)
