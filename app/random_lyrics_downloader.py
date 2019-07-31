from app.song import Song
import random


class RandomLyricsDownloader(object):
    def __init__(self, random_song_url_parser, lyrics_api_client):
        self.random_song_url_parser = random_song_url_parser
        self.lyrics_api_client = lyrics_api_client

    def get_random(self):
        song = self.random_song_url_parser.get_random_song()
        lyrics = self.lyrics_api_client.get_lyrics(song.artist, song.title)
        return Song(song.artist, song.title, lyrics)

    def get_random_by_artist(self, artist):
        songs = self.lyrics_api_client.find_all_songs_by_artist(artist)
        song = random.choice(songs)
        return Song(song.artist, song.title, song.lyrics)
