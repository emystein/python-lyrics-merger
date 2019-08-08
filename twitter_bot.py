import schedule
import time
import reply_to_mentions_bot
import periodic_tweet_bot

schedule.every(3).hours.do(periodic_tweet_bot.tweet_random_lyrics)
schedule.every().minute.do(reply_to_mentions_bot.reply_to_mentions)

def main():
	while True:
	   schedule.run_pending()
	   time.sleep(1)
	
if __name__ == "__main__":
	main()