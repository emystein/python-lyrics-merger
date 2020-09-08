import pytest
from unittest.mock import Mock
from twitter.twitter import TweetReply, ComposedReply
from twitter.tests.model import FakeTweet
from lyrics_mixer.song_titles_parser import ParsedArtists

def test_create_reply():
    tweet_parser = Mock()
    lyrics_mixer = Mock()

    tweet = FakeTweet(1, 'emenendez', '@lyricsmixer mix U2 and A-ha')

    tweet_parser.parse.return_value = ParsedArtists(['U2', 'A-ha'])
    lyrics_mixer.mix_random_lyrics_by_artists.return_value = 'Blah'

    tweet_reply = TweetReply(tweet).parse_with(tweet_parser).compose_reply(lyrics_mixer)

    assert tweet_reply == ComposedReply(tweet, 'Blah')
