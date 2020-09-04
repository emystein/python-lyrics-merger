class MixLyricsComposer:
    def __init__(self, lyrics_mixer):
        self.lyrics_mixer = lyrics_mixer

    def write_reply(self, tweet, parsed_song_titles):
        mixed_lyrics = self.lyrics_mixer.mix_parsed_song_titles(parsed_song_titles)

        return f"@{tweet.author.name} {mixed_lyrics}"