import requests
import urllib
from app.song import SongTitle


class WikiaSongUrlParser(object):
    def __init__(self):
        self.base_url = 'https://lyrics.fandom.com/wiki/'
        self.random_lyrics_url = self.base_url + 'special:randomincategory/Song'


    def get_random_song(self):
        response = requests.get(self.random_lyrics_url)
        return self.parse_url(response.url)


    def parse_url(self, url):
        unescaped_url = urllib.parse.unquote(url)
        artist, title = unescaped_url.replace(self.base_url, '').replace('_', ' ').split(':', 2)
        return SongTitle(artist, title)
