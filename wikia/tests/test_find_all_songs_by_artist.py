import pytest
from wikia.artist import ArtistRepository

def test_get_songs_by_artist_from_wikia():
	repository = ArtistRepository()
	all_songs = repository.find_all_songs_by_artist('Led Zeppelin')
	assert len(all_songs) == 156