import pytest
from unittest.mock import Mock
from twitter.twitter import Tweet
from twitter.tests.model import User, TweetForTest


def test_tweet_str():
    tweet_data = TweetForTest('emenendez', 'tweet text')

    tweet = Tweet(twitter_api =  Mock(), tweet = tweet_data)

    assert tweet.__str__() == 'Author: @emenendez, Text: tweet text'
