import logging
from lyrics_mixer.lyrics_mixers import RandomByArtistsLyricsMixer

logger = logging.getLogger()


class MixLyricsReplyStrategy(object):
    def __init__(self, lyrics_library, lyrics_mix_strategy):
        self.lyrics_library = lyrics_library
        self.lyrics_mix_strategy = lyrics_mix_strategy
    
    def write_reply(self, tweet, parsed):
        logger.info(f"Mixing lyrics requested by: {tweet.user.name}, using input: '{tweet.text}'")
        lyrics_mixer = RandomByArtistsLyricsMixer(lyrics_library, parsed.artist1, parsed.artist2)
        mixed_lyrics = lyrics_mixer.mix_lyrics(lyrics_mix_strategy)
        return f"@{tweet.user.name} {mixed_lyrics}"