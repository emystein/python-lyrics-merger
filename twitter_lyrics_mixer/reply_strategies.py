import logging


logger = logging.getLogger()


class MixLyricsReplyStrategy(object):
    def __init__(self, input_parser, lyrics_mixer):
        self.input_parser = input_parser
        self.lyrics_mixer = lyrics_mixer
    
    def get_reply_for(self, tweet):
        logger.info(f"Mixing lyrics requested by: {tweet.user.name}, using input: '{tweet.text}'")
        parsed = self.input_parser.parse(tweet.text)
        mixed_lyrics = self.lyrics_mixer.mix_random_lyrics_by_artists(parsed.artist1, parsed.artist2)
        return f"@{tweet.user.name} {mixed_lyrics}"