from twitter.twitter import ComposedReply

class MixLyricsComposer:
    def __init__(self, lyrics_mixer):
        self.lyrics_mixer = lyrics_mixer

    def reply(self, tweet, parsed_song_titles):
        lyrics = self.lyrics_mixer.mix_parsed_song_titles(parsed_song_titles)
        return ComposedReply(tweet, lyrics)
