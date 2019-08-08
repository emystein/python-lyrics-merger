import logging
import schedule
import time
from tweeter import create_api
import reply_to_mentions_bot
from periodic_tweet_bot import MixLyricsReplyStrategy, check_mentions

from lyrics_mixer.lyrics_mixer_app import LyricsMixerApp 
from lyrics_mixer.orm import StreamCursor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

api = create_api()

reply_strategy = MixLyricsReplyStrategy()

def reply_to_mentions():
    logger.info("Replying to mentions")
    cursor, created = StreamCursor.get_or_create(key = 'tweeter')
    cursor.position = check_mentions(api, cursor.position, reply_strategy)
    cursor.save()

# schedule.every(2).to(8).hours.do(periodic_tweet_bot.tweet_random_lyrics)
schedule.every().minute.do(reply_to_mentions)

def main():
	while True:
	   schedule.run_pending()
	   time.sleep(1)
	
if __name__ == "__main__":
	main()