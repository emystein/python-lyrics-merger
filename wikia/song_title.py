import requests
import urllib
import songs.model

class SongTitle:
    base_url = 'https://lyrics.fandom.com/wiki/'

    @staticmethod
    def parse_url(url):
        unescaped_url = urllib.parse.unquote(url)
        artist, title = unescaped_url.lstrip(SongTitle.base_url).replace('_', ' ').split(':', 2)
        return songs.model.SongTitle(artist, title)
    
    @staticmethod
    def random():
        response = requests.get(SongTitle.base_url + 'special:randomincategory/Song')
        return SongTitle.parse_url(response.url)
