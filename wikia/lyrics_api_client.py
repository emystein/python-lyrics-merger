import lyricwikia
import random
from lyrics_mixer.song import Song
from wikia.song_url_parser import WikiaSongUrlParser

def find_all_songs_by_artist(artist_name):
    artist = lyricwikia.Artist(artist_name)
    songs = []
    for album in artist.albums:
        songs.extend(album.songs)
    return songs


# TODO conver to module
class WikiaLyricsApiClient(object):
    def get_song(self, song_title):
        remote_song = lyricwikia.Song(song_title.artist, song_title.title)
        return Song(remote_song.artist, remote_song.title, remote_song.lyrics)

    def get_songs(self, song_titles):
        return [self.get_song(song_title) for song_title in song_titles]

    def get_random_song(self):
        song_url_parser = WikiaSongUrlParser()
        song_title = song_url_parser.get_random_song()
        remote_song = lyricwikia.Song(song_title.artist, song_title.title)
        return Song(remote_song.artist, remote_song.title, remote_song.lyrics)

    def get_random_songs(self, count):
        return [self.get_random_song() for _ in range(count)]

    def get_random_song_by_artist(self, artist):
        remote_songs = find_all_songs_by_artist(artist)
        remote_song = random.choice(remote_songs)
        return Song(remote_song.artist, remote_song.title, remote_song.lyrics)

    def get_random_songs_by_artists(self, artists):
        return [self.get_random_song_by_artist(artist) for artist in artists]

