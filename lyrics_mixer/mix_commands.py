from lyrics_mixer.song_titles_parser import ParsedSongTitles, ParsedArtists


class MixCommands:
    @staticmethod
    def select_for(parsed):
        mix_commands = [ArtistsMixCommand(), SongTitlesMixCommand()]

        return next(mix_command for mix_command in mix_commands if mix_command.accepts(parsed))


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