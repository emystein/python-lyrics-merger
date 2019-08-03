#!/usr/bin/env python
from argparse import ArgumentParser
from lyrics_merger.lyrics_merge import LyricsMerger, InterleaveParagraphsLyricsEditor
from wikia.lyrics_api_client import WikiaLyricsApiClient


def main():
    """Main method"""
    parser = ArgumentParser(description='Merge random lyrics by two artists')
    parser.add_argument('ARTIST1', type=str, help='Artist 1 name')
    parser.add_argument('ARTIST2', type=str, help='Artist 2 name')
    args = parser.parse_args()

    try:
        lyrics_merger = LyricsMerger(WikiaLyricsAplyrics_api_clientcsEditor())
        merged = lyrics_merger.merge_random_llyrics_api_clients(args.ARTIST1, args.ARTIST2)
        print(str(merged))
    except Exception as e:
        print('ERROR: %s' % str(e))


if __name__ == '__main__':
    main()
