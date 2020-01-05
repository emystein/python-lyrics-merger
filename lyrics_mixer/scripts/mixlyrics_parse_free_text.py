#!/usr/bin/env python
from argparse import ArgumentParser
from lyrics_mixer.artists_parser import ArtistsParser
from lyrics_mixer.lyrics_mixers import RandomByArtistsLyricsMixer
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix, ParagraphInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient


def main():
    """Main method"""
    parser = ArgumentParser(description='mix random lyrics by two artists')
    parser.add_argument('text', type=str, help='free text')
    args = parser.parse_args()

    try:
        artists_parser = ArtistsParser()
        artist1, artist2 = artists_parser.parse(args.text).artists
        lyrics_mixer = RandomByArtistsLyricsMixer(WikiaLyricsApiClient(), artist1, artist2)
        mixed_lyrics = lyrics_mixer.mix_lyrics(LineInterleaveLyricsMix())
        print(str(mixed_lyrics))
    except Exception as e:
        print('ERROR: %s' % str(e))


if __name__ == '__main__':
    main()
