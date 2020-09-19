from unittest.mock import Mock

import pytest

import twitter_bot.jobs
from lyrics_mixer.song_titles_parser import (
    ParsedArtists, SongTitlesParser, SongTitlesSplitter)
from lyrics_mixer.lyrics_mixer import MixedLyrics
from lyrics_mixer.tests.fixtures.mixer import mixed_song1_song2
from songs.model import ArtistTitle
from twitter_bot.twitter import Composer
from twitter_bot.tests.fixtures import tweet


tweet_parser = Mock()
lyrics_mixer = Mock()
reply_cursor = Mock()


def test_compose_reply(tweet, mixed_song1_song2):
    twitter_api = Mock()

    tweet_parser.parse.return_value = ParsedArtists(
        ArtistTitle('U2'), ArtistTitle('INXS'))

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = mixed_song1_song2

    composer = Composer(twitter_api, tweet_parser, lyrics_mixer)
    composer.reply(tweet)

    twitter_api.reply_tweet_with.assert_called_with(tweet, str(mixed_song1_song2))


def test_reply_to_mentions_empty_reply(tweet):
    twitter_api = Mock()

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = MixedLyrics.empty()

    composer = Composer(twitter_api, SongTitlesParser(SongTitlesSplitter()), lyrics_mixer)
    composer.reply(tweet)

    assert not twitter_api.reply_tweet_with.called


def test_job_tweet_random_lyrics(mixed_song1_song2):
    twitter_api = Mock()

    lyrics_mixer.mix_two_random_lyrics.return_value = mixed_song1_song2

    twitter_bot.jobs.tweet_random_lyrics(twitter_api, lyrics_mixer)

    twitter_api.update_status.assert_called_with(str(mixed_song1_song2))


def test_job_reply_to_mentions(tweet, mixed_song1_song2):
    twitter_api = Mock()

    twitter_api.mentions_since.return_value = [tweet]

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = mixed_song1_song2

    twitter_bot.jobs.reply_to_mentions(
        twitter_api, SongTitlesParser(SongTitlesSplitter()), lyrics_mixer, reply_cursor)

    twitter_api.reply_tweet_with.assert_called_with(tweet, str(mixed_song1_song2))
    reply_cursor.point_to.assert_called_with(tweet)
