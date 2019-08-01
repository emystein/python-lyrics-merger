import lyricwikia
from wikia.songs import SongRepository
from wikia.song_url_parser import WikiaSongUrlParser


class WikiaLyricsApiClient(object):
    def get_song(self, artist, title):
        return lyricwikia.Song(artist, title)


    def find_all_songs_by_artist(self, artist):
        song_repository = SongRepository()
        return song_repository.find_all_songs_by_artist(artist)


    def get_random_song(self):
        song_url_parser = WikiaSongUrlParser()
        remote_song = song_url_parser.get_random_song()
        return lyricwikia.Song(remote_song.artist, remote_song.title)
