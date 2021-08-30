import pytest

from lyrics_providers.azlyrics import Artist


def test_single_name():
    artist = Artist.named('Prince')

    assert artist.name == 'Prince'


def test_first_name_then_last_name():
    artist = Artist.named('Peter Gabriel')

    assert artist.name == 'Peter Gabriel'


def test_named_last_name_then_first_name():
    artist = Artist.named('Villere, Zack')

    assert artist.name == 'Zack Villere'


@pytest.mark.slow_integration_test
def test_lyrics_not_found():
    assert len(Artist.named('Menéndez').all_songs()) == 0


@pytest.mark.slow_integration_test
def test_get_songs_by_u2():
    artist = Artist.named('U2')

    assert len(artist.all_songs()) > 0
