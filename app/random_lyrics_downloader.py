import requests
import lyricwikia
from app.song import Song
from app.wikia_song_url_parser import WikiaSongUrlParser


class RandomLyricsDownloader(object):
    def __init__(self, random_lyrics_url):
        self.random_lyrics_url = random_lyrics_url
        self.song_url_parser = WikiaSongUrlParser()

    def download_next(self):
        response = requests.get(self.random_lyrics_url)
        print('\nLyrics URL: ' + response.url)
        song_info = self.song_url_parser.parse_url(response.url)
        lyrics = lyricwikia.get_lyrics(song_info.artist, song_info.title)
        return Song(song_info.artist, song_info.title, lyrics)
