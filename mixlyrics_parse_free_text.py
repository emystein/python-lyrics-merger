#!/usr/bin/env python
from argparse import ArgumentParser
import logging
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser
from lyrics_mixer.lyrics_mixer import LyricsMixer
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix
from lyrics_providers.azlyrics import AZLyricsLibrary
import sys

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def main():
    """Main method"""
    parser = ArgumentParser(description='mix random lyrics by two artists')
    parser.add_argument('text', type=str, help='free text')
    args = parser.parse_args()

    try:
        titles_parser = SongTitlesParser(SongTitlesSplitter())
        parsed_text = titles_parser.parse(args.text)
        print(str(parsed_text))
        lyrics_mixer = LyricsMixer(AZLyricsLibrary(), LineInterleaveLyricsMix())
        mixed = parsed_text.mix_using(lyrics_mixer)
        print(str(mixed))
    except Exception as e:
        print('ERROR: %s' % str(e))


if __name__ == '__main__':
    main()
