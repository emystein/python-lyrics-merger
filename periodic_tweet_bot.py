import time
import sys
import tweepy

from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient


# set vars in heroku dashboard
from os import environ
CONSUMER_KEY = environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = environ['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN = environ['TWITTER_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['TWITTER_ACCESS_TOKEN_SECRET']

TWEET_LENGTH = 210
PERIOD_IN_HOURS_BETWEEN_TWEETS = 3

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())

while True:
    print("About to mix lyrics")
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    tweet = str(mixed_lyrics)[:TWEET_LENGTH]
    api.update_status(tweet) 
    time.sleep(PERIOD_IN_HOURS_BETWEEN_TWEETS * 60 * 60)
