import time
import sys
import twitter

from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient

def tweet_random_lyrics(twitter_api):
    print("About to mix lyrics")
    lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    tweet = str(mixed_lyrics)[:twitter.MAX_TWEET_LENGTH]
    twitter_api.update_status(tweet) 
