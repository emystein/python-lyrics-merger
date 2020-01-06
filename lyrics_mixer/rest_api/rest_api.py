from flask import Flask, escape
from datetime import datetime
from lyrics_mixer.dispatcher import Dispatcher
from lyrics_mixer.lyrics_mixers import *
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient
from songs.model import SongTitle


def configure_views(app):
	@app.route('/')
	def home():
		return f'{datetime.now()}: OK\n'


	@app.route('/mix/random')
	def mix_two_random_lyrics(lyrics_library: WikiaLyricsApiClient, lyrics_mix_strategy: LineInterleaveLyricsMix):
		lyrics_mixer = RandomLyricsMixer(lyrics_library)
		mixed_lyrics = lyrics_mixer.mix_lyrics(lyrics_mix_strategy)
		return f'{escape(str(mixed_lyrics))}'


	@app.route('/mix/artists/<artist1>/<artist2>')
	def mix_random_lyrics_by_artists(lyrics_library: WikiaLyricsApiClient, lyrics_mix_strategy: LineInterleaveLyricsMix, artist1, artist2):
		lyrics_mixer = RandomByArtistsLyricsMixer(lyrics_library, artist1, artist2)
		mixed_lyrics = lyrics_mixer.mix_lyrics(lyrics_mix_strategy)
		return f'{escape(str(mixed_lyrics))}'


	@app.route('/mix/songs/<artist1>/<title1>/<artist2>/<title2>')
	def mix_two_specific_lyrics(lyrics_library: WikiaLyricsApiClient, lyrics_mix_strategy: LineInterleaveLyricsMix, artist1, title1, artist2, title2):
		song_title1 = SongTitle(artist1, title1)
		song_title2 = SongTitle(artist2, title2)
		lyrics_mixer = SpecificLyricsMixer(lyrics_library, song_title1, song_title2)
		mixed_lyrics = lyrics_mixer.mix_lyrics(lyrics_mix_strategy)
		return f'{escape(str(mixed_lyrics))}'

