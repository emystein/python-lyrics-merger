from unittest.mock import Mock

import pytest

from lyrics_mixer.lyrics_data_source import LyricsDataSource
from lyrics_mixer.lyrics_mixer import (LineInterleaveLyricsMix, LyricsMixer,
                                       MixedLyrics)
from lyrics_mixer.song_titles_parser import (SongTitlesParser,
                                             SongTitlesSplitter)
from twitter_bot.tests.model import FakeTweet
from twitter_bot.twitter import Composer, Tweet

twitter_api = Mock()
lyrics_mixer = Mock()


def test_reply_to_mentions_empty_reply():
    tweet = Tweet(twitter_api, FakeTweet(1, 'emystein', '@lyricsmixer mix U2 and INXS'))

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = MixedLyrics.empty()

    composer = Composer(SongTitlesParser(SongTitlesSplitter()), lyrics_mixer)
    composer.reply(tweet)

    assert not twitter_api.reply_tweet_with.called
