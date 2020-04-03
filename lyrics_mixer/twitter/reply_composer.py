import logging
from lyrics_mixer.mixed_lyrics import EmptyMixedLyrics


logger = logging.getLogger()


class MixLyricsReplyComposer:
    def __init__(self, lyrics_mixer):
        self.lyrics_mixer = lyrics_mixer

    def write_reply(self, tweet, parsed_data_from_tweet):
        mixed_lyrics = self.mix(parsed_data_from_tweet)
        return f"@{tweet.user.name} {mixed_lyrics}"

    def mix(self, parsed_song_titles):
        try:
            return parsed_song_titles.mix(self.lyrics_mixer)
        except Exception as e:
            logger.error('Returning empty lyrics.', exc_info=True)
            return EmptyMixedLyrics()
