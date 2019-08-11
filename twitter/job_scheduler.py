import schedule
import time
import twitter
import jobs
from twitter.twitter_api_wrapper import TwitterApiWrapper

twitter_api = twitter.create_api()
twitter_api_wrapper = TwitterApiWrapper(twitter_api)
    
schedule.every().minute.do(jobs.reply_to_mentions, twitter_api = twitter_api_wrapper)
schedule.every(6).hours.do(jobs.tweet_random_lyrics, twitter_api = twitter_api_wrapper)
    
def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
