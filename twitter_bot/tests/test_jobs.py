from lyrics_mixer.lyrics_data_source import LyricsDataSource
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, MixedLyrics
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser
from lyrics_mixer.tests.fixtures.mixer import mixed_song1_song2
import pytest
from unittest.mock import Mock
from twitter_bot.tests.model import FakeTweet
from twitter_bot.twitter import Tweet
import twitter_bot.jobs


twitter_api = Mock()
lyrics_mixer = Mock()
reply_cursor = Mock()

def test_random_lyrics(mixed_song1_song2):
    lyrics_mixer.mix_two_random_lyrics.return_value = mixed_song1_song2

    twitter_bot.jobs.tweet_random_lyrics(twitter_api, lyrics_mixer)

    twitter_api.update_status.assert_called_with(str(mixed_song1_song2))


def test_reply_to_mentions(mixed_song1_song2):
    tweet = Mock()
    tweet.id = 1
    tweet.text = '@lyricsmixer mezclá U2 y INXS'

    twitter_api.mentions_since.return_value = [tweet]

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = mixed_song1_song2

    twitter_bot.jobs.reply_to_mentions(
        twitter_api, SongTitlesParser(SongTitlesSplitter()), lyrics_mixer, reply_cursor)

    tweet.reply_with.assert_called_with(str(mixed_song1_song2))
    reply_cursor.point_to.assert_called_with(tweet)

