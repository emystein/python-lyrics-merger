import pytest
import lyrics_mixer.rest_api_context


@pytest.fixture
def app():
    return lyrics_mixer.rest_api_context.app

@pytest.mark.slow_integration_test
def test_root(client):
    response = client.get("/")

    assert response.status_code == 200

@pytest.mark.slow_integration_test
def test_mix_two_random_lyrics(client):
    response = client.get("/mix/random")

    assert response.status_code == 200

@pytest.mark.slow_integration_test
def test_mix_two_random_lyrics_by_artists(client):
    response = client.get("/mix/artists/Led_Zeppelin/Steppenwolf")

    assert response.status_code == 200

@pytest.mark.slow_integration_test
def test_mix_two_specific_lyrics(client):
    response = client.get("/mix/songs/Led_Zeppelin/Stairway_to_Heaven/Steppenwolf/Born_to_be_wild")

    assert response.status_code == 200
