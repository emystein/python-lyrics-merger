from flask import Flask, escape, request
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, ParagraphInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient


app = Flask(__name__)
lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())


@app.route('/mix/artists/<artist1>/<artist2>/')
def mix_artists(artist1, artist2):
	mixed = lyrics_mixer.mix_random_lyrics_by_artists(artist1, artist2)
	return f'{escape(str(mixed))}'
