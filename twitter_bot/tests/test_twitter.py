from lyrics_mixer.tests.fixtures.mixer import mixed_song1_song2
import pytest
from unittest.mock import Mock
from twitter_bot.twitter import Tweet, Composer
from twitter_bot.tests.model import FakeTweet
from lyrics_mixer.song_titles_parser import ArtistsParser

def test_compose_reply(mixed_song1_song2):
    tweet_parser = Mock()
    lyrics_mixer = Mock()
    twitter_api = Mock()
    
    origin_tweet = FakeTweet(1, 'emenendez', '@lyricsmixer mix U2 and A-ha')

    tweet = Tweet(twitter_api, origin_tweet)

    parser = ArtistsParser()
    parsed = parser.parse_song_titles(['U2', 'INXS'])

    tweet_parser.parse.return_value = parsed

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = mixed_song1_song2

    composer = Composer(tweet_parser, lyrics_mixer)
    composer.reply(tweet) 

    twitter_api.reply_tweet_with.assert_called_with(origin_tweet, str(mixed_song1_song2))


