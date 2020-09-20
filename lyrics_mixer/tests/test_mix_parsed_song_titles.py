import pytest
from lyrics_mixer.song_titles_parser import ParsedFullTitles, ParsedArtists
from lyrics_mixer.tests.fixtures.mixer import mixer
from songs.model import SongTitle, ArtistTitle


@pytest.mark.slow_integration_test
def test_mix_titles(mixer):
    parsed = ParsedFullTitles(SongTitle('U2', 'One'), SongTitle('INXS', 'Doctor'))

    mixed_lyrics = parsed.mix_using(mixer)

    assert mixed_lyrics.has_content()


@pytest.mark.slow_integration_test
def test_mix_artists(mixer):
    parsed = ParsedArtists(ArtistTitle('U2'), ArtistTitle('INXS'))

    mixed_lyrics = parsed.mix_using(mixer)

    assert mixed_lyrics.has_content()
