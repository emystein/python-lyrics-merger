from flask import Flask
from injector import Module, Injector, singleton
from flask_injector import FlaskInjector
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMixStrategy
from lyrics_mixer.lyrics_data_source import LyricsDataSource
from lyrics_mixer.rest_api import configure_views


class AppModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        lyrics_mixer = LyricsMixer(LyricsDataSource(), LineInterleaveLyricsMixStrategy())
        binder.bind(LyricsMixer, to=lyrics_mixer, scope=singleton)


app = Flask(__name__)
injector = Injector([AppModule(app)])
configure_views(app=app)
FlaskInjector(app=app, injector=injector)
