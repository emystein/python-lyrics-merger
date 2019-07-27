import lyricwikia
from wikia.songs import SongRepository


class WikiaLyricsApiClient(object):
    def get_lyrics(self, artist, title):
        return lyricwikia.get_lyrics(artist, title)

    def find_all_songs_by_artist(self, artist):
        song_repository = SongRepository()
        return song_repository.find_all_songs_by_artist(artist)
