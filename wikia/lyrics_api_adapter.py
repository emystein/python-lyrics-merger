import lyricwikia
from wikia.artist import ArtistRepository


class WikiaLyricsAdapter(object):
    def get_lyrics(self, artist, title):
        return lyricwikia.get_lyrics(artist, title)

    def find_all_songs_by_artist(self, artist):
        artist_repository = ArtistRepository()
        songs = artist_repository.find_all_songs_by_artist(artist)
        return songs
