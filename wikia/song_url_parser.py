import requests
import urllib
from songs.model import SongTitle


base_url = 'https://lyrics.fandom.com/wiki/'

random_lyrics_url = base_url + 'special:randomincategory/Song'


def get_random_song():
    response = requests.get(random_lyrics_url)
    return parse_url(response.url)


def parse_url(url):
    unescaped_url = urllib.parse.unquote(url)
    artist, title = unescaped_url.lstrip(base_url).replace('_', ' ').split(':', 2)
    return SongTitle(artist, title)
