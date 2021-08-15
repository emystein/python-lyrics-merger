import pytest

from lyrics_providers.azlyrics import random_artist, Artist


def test_single_name():
    artist = Artist.named('Prince')

    assert artist.name == 'Prince'


def test_first_name_then_last_name():
    artist = Artist.named('Peter Gabriel')

    assert artist.name == 'Peter Gabriel'


def test_named_last_name_then_first_name():
    artist = Artist.named('Villere, Zack')

    assert artist.name == 'Zack Villere'


