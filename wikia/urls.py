import requests
from urllib.parse import unquote

def base_url():
  return 'https://lyrics.fandom.com/wiki/'

def random_song_url():
  random_song_url = base_url() + 'special:randomincategory/Song'
  return requests.get(random_song_url).url

def song_title_from(url_to_parse):
  return unquote(url_to_parse).lstrip(base_url()).replace('_', ' ').split(':', 2)
