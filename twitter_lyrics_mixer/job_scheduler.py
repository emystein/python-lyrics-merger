import logging
import schedule
import time
import jobs
from lyrics_mixer.artists_parser import ArtistsParser
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient
from twitter.twitter_api_wrapper import TwitterApiWrapper
from reply_strategies import MixLyricsReplyStrategy

logging.basicConfig(level=logging.INFO)

twitter_api_wrapper = TwitterApiWrapper()

lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())
reply_strategy = MixLyricsReplyStrategy(ArtistsParser(), lyrics_mixer) 

schedule.every().minute.do(jobs.reply_to_mentions, twitter_api = twitter_api_wrapper, reply_strategy = reply_strategy)
schedule.every(6).hours.do(jobs.tweet_random_lyrics, twitter_api = twitter_api_wrapper, lyrics_mixer = lyrics_mixer)
    
def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
