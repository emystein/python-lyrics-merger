import logging
from lyrics_mixer.mix_commands import ArtistsMixCommand, SongTitlesMixCommand

logger = logging.getLogger()


class MixLyricsReplyStrategy:
    def __init__(self, lyrics_mixer):
        self.lyrics_mixer = lyrics_mixer

    def write_reply(self, tweet, mix_command):
        logger.info(f"Replying to: {tweet.user.name}, mention: '{tweet.text}'")
        try:
            mixed_lyrics = mix_command.mix(self.lyrics_mixer)
        except Exception as e:
            logger.error('Returning empty lyrics.', exc_info=True)
            mixed_lyrics = EmptyMixedLyrics()
        return f"@{tweet.user.name} {mixed_lyrics}"
