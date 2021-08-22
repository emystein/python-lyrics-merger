import pytest

from lyrics_providers.azlyrics import random_artist, Artist


@pytest.mark.slow_integration_test
def test_random():
    artist = random_artist()

    assert artist.name != ''
    assert len(artist.all_songs()) > 0


@pytest.mark.slow_integration_test
def test_get_songs_by_artist():
    artist = Artist.named('Led Zeppelin')

    assert len(artist.all_songs()) > 80

    song = artist.random_song()

    assert not song.title.is_empty()
    assert song.title.artist == 'Led Zeppelin'
    assert song.has_lyrics()


@pytest.mark.slow_integration_test
def test_lyrics_not_found():
    assert len(Artist.named('Menéndez').all_songs()) == 0


@pytest.mark.slow_integration_test
def test_get_songs_by_u2():
    artist = Artist.named('U2')

    assert len(artist.all_songs()) > 0
