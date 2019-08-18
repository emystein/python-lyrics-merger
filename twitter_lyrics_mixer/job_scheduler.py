import logging
import schedule
import threading
import time
import jobs
from lyrics_mixer.artists_parser import ArtistsParser
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient
from twitter.twitter import TwitterApi, TweetReplyFactory
from reply_strategies import MixLyricsReplyStrategy

logging.basicConfig(level=logging.INFO)

twitter_api = TwitterApi()

lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())

schedule.every().minute.do(run_threaded, jobs.reply_to_mentions, twitter_api = twitter_api, tweet_reply_factory = TweetReplyFactory(ArtistsParser(), MixLyricsReplyStrategy(lyrics_mixer)))
schedule.every(6).hours.do(run_threaded, jobs.tweet_random_lyrics, twitter_api = twitter_api, lyrics_mixer = lyrics_mixer)
    
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
