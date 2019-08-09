import threading
import schedule
import time
from tweeter import create_api
import periodic_tweet_bot
import reply_to_mentions_bot
    

api = create_api()
    
schedule.every().minute.do(reply_to_mentions_bot.reply_to_mentions, twitter_api = api)
schedule.every(2).to(8).hours.do(periodic_tweet_bot.tweet_random_lyrics, twitter_api = api)
    
def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
