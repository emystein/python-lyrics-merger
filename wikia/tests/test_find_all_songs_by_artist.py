import pytest
from wikia.songs import SongRepository

def test_get_songs_by_artist_from_wikia():
	repository = SongRepository()
	all_songs = repository.find_all_songs_by_artist('Led Zeppelin')
	assert len(all_songs) == 156