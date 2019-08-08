import time
import sys
from tweeter import create_api

from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient


MAX_TWEET_LENGTH = 280
PERIOD_IN_HOURS_BETWEEN_TWEETS = 3


def tweet_random_lyrics():
    api = create_api()
    print("About to mix lyrics")
    lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    tweet = str(mixed_lyrics)[:MAX_TWEET_LENGTH]
    api.update_status(tweet) 


def main():
    print("About to mix lyrics")
    api = create_api()
    lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    tweet = str(mixed_lyrics)[:MAX_TWEET_LENGTH]
    api.update_status(tweet) 
    time.sleep(PERIOD_IN_HOURS_BETWEEN_TWEETS * 60 * 60)


if __name__ == "__main__":
    main()
