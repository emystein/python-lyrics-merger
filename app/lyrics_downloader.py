import requests
from app.song import Song


class LyricsDownloader(object):
    def __init__(self, random_lyrics_url, song_url_parser, lyrics_api_adapter):
        self.random_lyrics_url = random_lyrics_url
        # Pass song_url_parser as constructor parameter to generalize this class
        self.song_url_parser = song_url_parser
        self.lyrics_api_adapter = lyrics_api_adapter

    def download_next(self):
        response = requests.get(self.random_lyrics_url)
        song_info = self.song_url_parser.parse_url(response.url)
        lyrics = self.lyrics_api_adapter.get_lyrics(
            song_info.artist, song_info.title)
        return Song(song_info.artist, song_info.title, lyrics)
