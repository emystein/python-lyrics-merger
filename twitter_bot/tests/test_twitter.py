import pytest
from unittest.mock import Mock
from twitter_bot.twitter import Composer, ComposedReply
from twitter_bot.tests.model import FakeTweet
from lyrics_mixer.song_titles_parser import ArtistsParser

def test_compose_reply():
    tweet_parser = Mock()
    lyrics_mixer = Mock()

    tweet = FakeTweet(1, 'emenendez', '@lyricsmixer mix U2 and A-ha')

    parser = ArtistsParser()
    parsed = parser.parse_song_titles(['U2', 'INXS'])

    tweet_parser.parse.return_value = parsed

    lyrics_mixer.mix_random_lyrics_by_artists.return_value = 'Blah'

    composer = Composer(tweet_parser, lyrics_mixer)
    
    assert composer.compose_reply(tweet) == ComposedReply(tweet, 'Blah')
