import logging


logger = logging.getLogger()


class MixLyricsReplyStrategy(object):
    def __init__(self, lyrics_mixer):
        self.lyrics_mixer = lyrics_mixer
    
    def write_reply(self, tweet, parsed):
        logger.info(f"Mixing lyrics requested by: {tweet.user.name}, using input: '{tweet.text}'")
        try:
            mixed_lyrics = self.lyrics_mixer.mix_random_lyrics_by_artists(parsed.artist1, parsed.artist2)
        except Exception as e:
            logger.error('Error picking songs, returning empty lyrics.', exc_info=True)
            mixed_lyrics = EmptyMixedLyrics()
        return f"@{tweet.user.name} {mixed_lyrics}"