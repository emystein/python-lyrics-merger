import pytest
from unittest.mock import Mock
from twitter.twitter import Tweet
from lyrics_mixer.twitter.tests.model import User, TweetForTest


def test_tweet_str():
    api = Mock()

    tweet_data = TweetForTest('emenendez', 'tweet text')

    tweet_wrapper = Tweet(api, tweet_data)

    assert tweet_wrapper.__str__() == 'Author: @emenendez, Text: tweet text'
