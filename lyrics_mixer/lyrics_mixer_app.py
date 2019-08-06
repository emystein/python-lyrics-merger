import logging
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, EmptyMixedLyrics
from wikia.lyrics_api_client import WikiaLyricsApiClient
from lyrics_mixer.artists_parser import ArtistsParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class LyricsMixerApp(object):
    def __init__(self):
        self.input_parser = ArtistsParser()
        self.mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())

    def mix_lyrics_parsing_input(self, text):
        try:
            parsed = self.input_parser.parse(text)
            mixed_lyrics = self.mixer.mix_random_lyrics_by_artists(parsed.artist1, parsed.artist2)
        except Exception as e:
            logger.error("Error mixing lyrics, returning empty lyrics", exc_info=True)
            mixed_lyrics = EmptyMixedLyrics()
        logger.info(f"Mixed lyrics: {mixed_lyrics.title}")
        return mixed_lyrics
