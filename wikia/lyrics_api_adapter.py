import lyricwikia
from wikia.songs import SongRepository
from wikia.random_song_url_parser import WikiaRandomSongUrlParser


class WikiaLyricsApiClient(object):
    def get_lyrics(self, artist, title):
        return lyricwikia.Song(artist, title)


    def find_all_songs_by_artist(self, artist):
        song_repository = SongRepository()
        return song_repository.find_all_songs_by_artist(artist)


    def get_random_lyrics(self):
        random_song_url_parser = WikiaRandomSongUrlParser()
        remote_song = random_song_url_parser.get_random_song()
        return lyricwikia.Song(remote_song.artist, remote_song.title)
