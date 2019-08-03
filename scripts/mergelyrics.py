#!/usr/bin/env python
from argparse import ArgumentParser
from lyrics_merger.lyrics_merge import LyricsMerger, LyricsEditor
from wikia.lyrics_api_client import WikiaLyricsApiClient


def main():
    """Main method"""
    parser = ArgumentParser(description='Merge random lyrics by two artists')
    parser.add_argument('ARTIST1', type=str, help='Artist 1 name')
    parser.add_argument('ARTIST2', type=str, help='Artist 2 name')
    args = parser.parse_args()

    try:
        lyrics_merger = LyricsMerger(WikiaLyricsApiClient(), LyricsEditor())
        merged = lyrics_merger.merge_random_lyrics_by_artists(args.ARTIST1, args.ARTIST2)
        lyrics_report = merged.title + '\n\n' + merged.text
        print(lyrics_report)
    except Exception as e:
        print('ERROR: %s' % str(e))


if __name__ == '__main__':
    main()
