import pytest
from lyrics_mixer.song_titles_parser import ParsedSongTitles, ParsedArtists
from lyrics_mixer.tests.fixtures.mixer import mixer


@pytest.mark.slow_integration_test
def test_mix_titles(mixer):
    parsed = ParsedSongTitles(['U2 - One', 'INXS - Doctor'])

    mixed_lyrics = parsed.mix_using(mixer)

    assert mixed_lyrics.has_content()


@pytest.mark.slow_integration_test
def test_mix_artists(mixer):
    parsed = ParsedArtists(['U2', 'INXS'])

    mixed_lyrics = parsed.mix_using(mixer)

    assert mixed_lyrics.has_content()
