import logging
from lyrics_mixer.mixed_lyrics import EmptyMixedLyrics


logger = logging.getLogger()


class MixLyricsComposer:
    def __init__(self, lyrics_mixer):
        self.lyrics_mixer = lyrics_mixer

    def write_reply(self, tweet, parsed_song_titles):
        mixed_lyrics = self.mix(parsed_song_titles)
        return f"@{tweet.user.name} {mixed_lyrics}"

    def mix(self, parsed_song_titles):
        try:
            return self.lyrics_mixer.mix_parsed_song_titles(parsed_song_titles)
        except Exception as e:
            logger.error('Returning empty lyrics.', exc_info=True)
            return EmptyMixedLyrics()
