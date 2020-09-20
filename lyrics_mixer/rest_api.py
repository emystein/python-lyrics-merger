from datetime import datetime

from flask import Flask, escape
from flask_injector import FlaskInjector
from injector import Module, Injector, singleton

from lyrics_mixer.lyrics_data_source import LyricsDataSource
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix


def configure_views(app):
    @app.route('/')
    def home():
        return f'{datetime.now()}: OK\n'

    @app.route('/mix/random')
    def mix_two_random_lyrics(lyrics_mixer: LyricsMixer):
        mixed = lyrics_mixer.mix_two_random_lyrics()
        return f'{escape(str(mixed))}'

    @app.route('/mix/artists/<artist1>/<artist2>')
    def mix_random_lyrics_by_artists(lyrics_mixer: LyricsMixer, artist1, artist2):
        mixed = lyrics_mixer.mix_random_lyrics_by_artists(artist1, artist2)
        return f'{escape(str(mixed))}'

    @app.route('/mix/songs/<artist1>/<title1>/<artist2>/<title2>')
    def mix_two_specific_lyrics(lyrics_mixer: LyricsMixer, artist1, title1, artist2, title2):
        mixed = lyrics_mixer.mix_two_specific_lyrics(artist1, title1, artist2, title2)
        return f'{escape(str(mixed))}'


lyrics_mixer = LyricsMixer(LyricsDataSource(), LineInterleaveLyricsMix())


class AppModule(Module):
    def __init__(self, app, lyrics_mixer):
        self.app = app
        self.lyrics_mixer = lyrics_mixer

    def configure(self, binder):
        binder.bind(LyricsMixer, to=self.lyrics_mixer, scope=singleton)


app = Flask(__name__)
injector = Injector([AppModule(app, lyrics_mixer)])
configure_views(app=app)
FlaskInjector(app=app, injector=injector)
