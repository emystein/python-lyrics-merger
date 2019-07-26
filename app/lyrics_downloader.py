import requests
from app.song import Song


class RandomLyricsDownloader(object):
    def __init__(self, random_lyrics_url, song_url_parser, lyrics_api_adapter):
        self.random_lyrics_url = random_lyrics_url
        self.song_url_parser = song_url_parser
        self.lyrics_api_adapter = lyrics_api_adapter

    def download_random_lyrics(self):
        response = requests.get(self.random_lyrics_url)
        song = self.song_url_parser.parse_url(response.url)
        lyrics = self.lyrics_api_adapter.get_lyrics(song.artist, song.title)
        return Song(song.artist, song.title, lyrics)
