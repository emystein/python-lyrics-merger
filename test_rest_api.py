import pytest
from unittest.mock import Mock
from flask import Flask 
from injector import Module, Injector, singleton
from flask_injector import FlaskInjector
from lyrics_mixer.lyrics_mixer import LyricsMixer
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix, ParagraphInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient
# from rest_api import configure_views
import rest_api_context


# class AppModule(Module):
#     def __init__(self, app):
#         self.app = app

#     def configure(self, binder):
#         lyrics_mixer = LyricsMixer(
#             WikiaLyricsApiClient(), LineInterleaveLyricsMix())
#         binder.bind(LyricsMixer, to=lyrics_mixer, scope=singleton)


# @pytest.fixture
# def app():
#     app = Flask(__name__)
#     injector = Injector([AppModule(app)])
#     configure_views(app=app)
#     FlaskInjector(app=app, injector=injector)
#     return app

@pytest.fixture
def app():
    return rest_api_context.app

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200


def test_mix_two_random_lyrics(client):
    response = client.get("/mix/random")
    assert response.status_code == 200


def test_mix_two_random_lyrics_by_artists(client):
    response = client.get("/mix/artists/Led_Zeppelin/Steppenwolf")
    assert response.status_code == 200


def test_mix_two_specific_lyrics(client):
    response = client.get("/mix/songs/Led_Zeppelin/Stairway_to_Heaven/Steppenwolf/Born_to_be_wild")
    assert response.status_code == 200
