import pytest
import lyrics_mixer.song_titles_parser
from songs.model import SongTitle
import tests.song_title_factory
from tests.fixtures.song_titles import song_title1, song_title2


@pytest.mark.usefixtures('song_title1', 'song_title2')
@pytest.mark.parametrize('song_titles_separator', [', ', ' y '])
def test_parse_song_titles_(song_title1, song_title2, song_titles_separator):
    result = lyrics_mixer.song_titles_parser.parse(
        str(song_title1) + song_titles_separator + str(song_title2))
    assert result.song_titles == [song_title1, song_title2]
