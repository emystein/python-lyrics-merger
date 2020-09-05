from twitter.twitter import ComposedReply

class MixLyricsComposer:
    def __init__(self, lyrics_mixer):
        self.lyrics_mixer = lyrics_mixer

    def reply(self, tweet, parsed_song_titles):
        lyrics = parsed_song_titles.mix_using(self.lyrics_mixer)
        return ComposedReply(tweet, lyrics)
