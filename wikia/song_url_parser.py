import requests
import urllib
from app.song import SongTitle


class WikiaSongUrlParser(object):
    def __init__(self):
        self.random_lyrics_url = 'https://lyrics.fandom.com/wiki/special:randomincategory/Song'


    def get_random_song(self):
        response = requests.get(self.random_lyrics_url)
        return self.parse_url(response.url)


    def parse_url(self, url):
        unescaped_url = urllib.parse.unquote(url)
        artist, title = unescaped_url.replace(
            '_', ' ').rsplit('/', 1)[-1].split(':', 2)
        return SongTitle(artist, title)
