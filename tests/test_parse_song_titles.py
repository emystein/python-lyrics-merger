import pytest
import lyrics_mixer.song_titles_parser
from lyrics_mixer.song import SongTitle
import tests.song_title_factory


@pytest.fixture
def song_title1():
    return tests.song_title_factory.create_stairway_to_heaven()


@pytest.fixture
def song_title2():
    return tests.song_title_factory.create_born_to_be_wild()


@pytest.mark.parametrize('song_titles_separator', [', ', ' y '])
def test_parse_song_titles_(song_title1, song_title2, song_titles_separator):
    result = lyrics_mixer.song_titles_parser.parse(
        str(song_title1) + song_titles_separator + str(song_title2))
    assert result.song_titles == [song_title1, song_title2]
