from unittest.mock import Mock

import pytest

from lyrics_mixer.lyrics_data_source import LyricsDataSource
from lyrics_mixer.lyrics_mixer import LineInterleaveLyricsMix, MixedLyrics
from lyrics_mixer.song_titles_parser import SongTitlesParser, SongTitlesSplitter
from twitter_bot.twitter import Composer


def test_reply_to_mentions_empty_reply():
    tweet = Mock()
    tweet.text = '@lyricsmixer mezclá U2 y INXS'

    lyrics_mixer = Mock()
    lyrics_mixer.mix_random_lyrics_by_artists.return_value = MixedLyrics.empty()

    composer = Composer(SongTitlesParser(SongTitlesSplitter()), lyrics_mixer)
    composer.reply(tweet)

    assert not tweet.reply_with.called
