import abc
from songs.model import SongTitle, EmptySongTitle, ArtistOnlySongTitle


class Mixable:
    @abc.abstractmethod
    def mix_command(self):
        pass

    def mix(self, lyrics_mixer):
        self.mix_command().mix(lyrics_mixer)


class ParsedSongTitles(Mixable):
    def __init__(self, split_text):
        if self.accepts(split_text):
            artist, title = split_text[0].split(' - ')
            self.song_title1 = SongTitle(artist, title)
            artist, title = split_text[1].split(' - ')
            self.song_title2 = SongTitle(artist, title)
        else:
            self.song_title1 = EmptySongTitle()
            self.song_title2 = EmptySongTitle()
    
    def accepts(self, split_text):
        return '-' in split_text[0]
    
    def mix_command(self):
        return SongTitlesMixCommand()


class ParsedArtists(Mixable):
    def __init__(self, split_text):
        if self.accepts(split_text):
            self.song_title1 = ArtistOnlySongTitle(split_text[0])
            self.song_title2 = ArtistOnlySongTitle(split_text[1])
        else:
            self.song_title1 = EmptySongTitle()
            self.song_title2 = EmptySongTitle()

    def accepts(self, split_text):
        return '-' not in split_text[0]

    def mix_command(self):
        return ArtistsMixCommand()


class ArtistsMixCommand:
    def accepts(self, parsed):
        return isinstance(parsed, ParsedArtists)

    def mix(self, parsed, lyrics_mixer):
        return lyrics_mixer.mix_random_lyrics_by_artists(parsed.song_title1.artist, parsed.song_title2.artist)


class SongTitlesMixCommand:
    def accepts(self, parsed):
        return isinstance(parsed, ParsedSongTitles)

    def mix(self, parsed, lyrics_mixer):
        return lyrics_mixer.mix_two_specific_lyrics(parsed.song_title1, parsed.song_title2)
