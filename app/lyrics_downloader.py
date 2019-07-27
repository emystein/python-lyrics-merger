import requests
from app.song import Song
import random

class RandomLyricsDownloader(object):
    def __init__(self, random_lyrics_url, song_url_parser, lyrics_api_client):
        self.random_lyrics_url = random_lyrics_url
        self.song_url_parser = song_url_parser
        self.lyrics_api_client = lyrics_api_client

    def download_random_lyrics(self):
        response = requests.get(self.random_lyrics_url)
        song = self.song_url_parser.parse_url(response.url)
        lyrics = self.lyrics_api_client.get_lyrics(song.artist, song.title)
        return Song(song.artist, song.title, lyrics)
    
    def download_random_lyrics_by_artist(self, artist):
        songs = self.lyrics_api_client.find_all_songs_by_artist(artist)
        random_song = random.choice(songs)
        return Song(random_song.artist, random_song.title, random_song.lyrics)
