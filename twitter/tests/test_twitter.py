import pytest
from unittest.mock import Mock
from twitter.twitter import TweetReply, ComposedReply
from twitter.tests.model import FakeTweet
from lyrics_mixer.song_titles_parser import ParsedArtists

def test_create_reply():
    tweet_parser = Mock()
    composer = Mock()

    tweet = FakeTweet(1, 'emenendez', '@lyricsmixer mix U2 and A-ha')

    tweet_parser.parse.return_value = ParsedArtists(['U2', 'A-ha'])
    composer.reply.return_value = ComposedReply(tweet, 'Blah')

    tweet_reply = TweetReply(tweet).parse_with(tweet_parser).compose_reply(composer)

    assert tweet_reply == ComposedReply(tweet, 'Blah')
