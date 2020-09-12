#!/usr/bin/env python
from argparse import ArgumentParser
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser
from lyrics_mixer.lyrics_mixer import LyricsMixer
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMixStrategy, ParagraphInterleaveLyricsMixStrategy
from lyrics_mixer.lyrics_data_source import LyricsDataSource


def main():
    """Main method"""
    parser = ArgumentParser(description='mix random lyrics by two artists')
    parser.add_argument('text', type=str, help='free text')
    args = parser.parse_args()

    try:
        titles_parser = SongTitlesParser(SongTitlesSplitter())
        mix_command = titles_parser.parse(args.text)
        lyrics_mixer = LyricsMixer(
            LyricsDataSource(), LineInterleaveLyricsMixStrategy())
        mixed = mix_command.mix(lyrics_mixer)
        print(str(mixed))
    except Exception as e:
        print('ERROR: %s' % str(e))


if __name__ == '__main__':
    main()
