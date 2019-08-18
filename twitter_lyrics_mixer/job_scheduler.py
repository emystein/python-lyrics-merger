import logging
import schedule
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

schedule.every().minute.do(jobs.reply_to_mentions, twitter_api = twitter_api, tweet_reply_factory = TweetReplyFactory(ArtistsParser(), MixLyricsReplyStrategy(lyrics_mixer)))
schedule.every(3).hours.do(jobs.tweet_random_lyrics, twitter_api = twitter_api, lyrics_mixer = lyrics_mixer).run()
    
def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
