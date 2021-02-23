from unittest.mock import Mock

import pytest

import twitter_bot.jobs
from lyrics_mixer.song_titles_parser import (SongTitlesParser, SongTitlesSplitter)
from lyrics_mixer.lyrics_mixer import MixedLyrics
from lyrics_mixer.tests.fixtures.mixer import mixed_lyrics
from twitter_bot.twitter import MentionHistory, Composer
from twitter_bot.tests.fixtures import tweet

tweet_parser = SongTitlesParser(SongTitlesSplitter())
lyrics_mixer = Mock()
reply_cursor = Mock()


def test_compose_reply(tweet, mixed_lyrics):
    twitter_api = Mock()

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = mixed_lyrics

    composer = Composer(twitter_api, tweet_parser, lyrics_mixer)
    composer.reply(tweet)

    twitter_api.reply_tweet_with.assert_called_with(tweet, str(mixed_lyrics))


def test_reply_to_mentions_empty_reply(tweet):
    twitter_api = Mock()

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = MixedLyrics.empty()

    composer = Composer(twitter_api, tweet_parser, lyrics_mixer)
    composer.reply(tweet)

    assert not twitter_api.reply_tweet_with.called


def test_tweet(mixed_lyrics):
    twitter_api = Mock()

    composer = Composer(twitter_api, tweet_parser, lyrics_mixer)
    composer.tweet(mixed_lyrics)

    twitter_api.update_status.assert_called_with(str(mixed_lyrics))



