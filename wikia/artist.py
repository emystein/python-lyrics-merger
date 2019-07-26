from lyricwikia import Artist

class ArtistRepository(object):
	def find_all_songs_by_artist(self, artist_name):
		artist = Artist(artist_name)
		songs = [] 
		for album in artist.albums:
			songs.extend(album.songs)
		return songs
