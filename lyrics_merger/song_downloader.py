from lyrics_merger.song import Song
import random


class SongDownloader(object):
    def __init__(self, lyrics_api_client):
        self.lyrics_api_client = lyrics_api_client

    def get_random(self):
        remote_song = self.lyrics_api_client.get_random_song()
        return Song(remote_song.artist, remote_song.title, remote_song.lyrics)

    def get_random_by_artist(self, artist):
        remote_songs = self.lyrics_api_client.find_all_songs_by_artist(artist)
        remote_song = random.choice(remote_songs)
        return Song(remote_song.artist, remote_song.title, remote_song.lyrics)
