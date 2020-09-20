import pytest
from flask_injector import FlaskInjector
from injector import Injector

import lyrics_mixer.rest_api
from lyrics_mixer.lyrics_mixer import LyricsMixer, MixedLyrics
from lyrics_mixer.rest_api import AppModule


class LyricsMixerStub(LyricsMixer):
    def __init__(self):
        pass

    def mix_two_random_lyrics(self):
        return MixedLyrics.empty()

    def mix_random_lyrics_by_artists(self, artist1, artist2):
        return MixedLyrics.empty()

    def mix_two_specific_lyrics(self, artist1, title1, artist2, title2):
        return MixedLyrics.empty()


@pytest.fixture
def app():
    app = lyrics_mixer.rest_api.app
    injector = Injector([AppModule(app, LyricsMixerStub())])
    FlaskInjector(app=app, injector=injector)
    return app


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
