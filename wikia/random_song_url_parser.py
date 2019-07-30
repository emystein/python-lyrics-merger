import requests
from wikia.song_url_parser import WikiaSongUrlParser


class WikiaRandomSongUrlParser(object):
    def __init__(self):
        self.random_lyrics_url = 'https://lyrics.fandom.com/wiki/special:randomincategory/Song'

    def get_random_song(self):
        response = requests.get(self.random_lyrics_url)
        song_url_parser = WikiaSongUrlParser()
        return song_url_parser.parse_url(response.url)
