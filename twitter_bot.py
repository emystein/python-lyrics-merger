import schedule
import time
import reply_to_mentions_bot
import periodic_tweet_bot
from tweeter import create_api

api = create_api()

# schedule.every(2).to(8).hours.do(periodic_tweet_bot.tweet_random_lyrics)
schedule.every().minute.do(reply_to_mentions_bot.reply_to_mentions(api))

def main():
	while True:
	   schedule.run_pending()
	   time.sleep(1)
	
if __name__ == "__main__":
	main()