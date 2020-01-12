from songs.model import SongTitle

artist_song_separator = '-'

class ArtistsMixCommand:
    def __init__(self, artists):
        self.artists = artists
        self.artist1, self.artist2 = artists[0], artists[1]
        self.song_titles = []

    def accepts(self, text):
        return artist_song_separator not in text

    def mix(self, lyrics_mixer):
        return lyrics_mixer.mix_random_lyrics_by_artists(self.artist1, self.artist2)


class SongTitlesMixCommand:
    def __init__(self, titles):
        self.song_titles = list(
            map(lambda title: self.split_artist_and_title(title), titles))

    def split_artist_and_title(self, artist_and_title):
        if self.accepts(artist_and_title):
            artist, title = artist_and_title.split('-')
            return SongTitle(artist, title)
        else:
            return None

    def accepts(self, text):
        return artist_song_separator in text

    def mix(self, lyrics_mixer):
        return lyrics_mixer.mix_two_specific_lyrics(self.song_titles[0], self.song_titles[1])
