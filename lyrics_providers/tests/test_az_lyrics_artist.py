import pytest

from lyrics_providers.azlyrics import Artist


def test_random_initial():
    allowed_letters = list('abcdefghijklmnopqrstuvwxyz#')

    initial = Artist.random_initial()

    assert initial in allowed_letters


def test_named_last_name_then_first_name():
    artist = Artist.named('Villere, Zack')

    assert artist.name == 'Zack Villere'


@pytest.mark.slow_integration_test
def test_random():
    artist = Artist.random()

    assert artist.name != ''
    assert len(artist.all_songs()) > 0


@pytest.mark.slow_integration_test
def test_get_songs_by_artist():
    artist = Artist.named('Led Zeppelin')

    assert len(artist.all_songs()) > 80

    song = artist.random_song()

    assert song.artist == 'Led Zeppelin'
    assert not song.title.is_empty()
    assert song.has_lyrics()


@pytest.mark.slow_integration_test
def test_lyrics_not_found():
    assert len(Artist.named('Menéndez').all_songs()) == 0
