import time
import sys
import tweepy

from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, ParagraphInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient
from lyrics_mixer.song import SongTitle

# from credentials import *  # use this one for testing

# use this for production; set vars in heroku dashboard
from os import environ
CONSUMER_KEY = environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = environ['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN = environ['TWITTER_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['TWITTER_ACCESS_TOKEN_SECRET']

INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 60  # every 60 seconds, for testing

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())

while True:
    print("About to mix lyrics")
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    tweet = str(mixed_lyrics)[:280]
    api.update_status(tweet) 
    time.sleep(INTERVAL)
