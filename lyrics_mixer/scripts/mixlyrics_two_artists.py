#!/usr/bin/env python
from argparse import ArgumentParser
from lyrics_mixer.lyrics_mixer import LyricsMixer
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix, ParagraphInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient


def main():
    """Main method"""
    parser = ArgumentParser(description='mix random lyrics by two artists')
    parser.add_argument('ARTIST1', type=str, help='Artist 1 name')
    parser.add_argument('ARTIST2', type=str, help='Artist 2 name')
    args = parser.parse_args()

    try:
        lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())
        mixed = lyrics_mixer.mix_random_lyrics_by_artists(args.ARTIST1, args.ARTIST2)
        print(str(mixed))
    except Exception as e:
        print('ERROR: %s' % str(e))


if __name__ == '__main__':
    main()
lyrics_mix_strategy