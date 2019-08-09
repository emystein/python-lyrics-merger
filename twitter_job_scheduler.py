import schedule
import time
import twitter
import twitter_jobs

twitter_api = twitter.create_api()
    
schedule.every().minute.do(twitter_jobs.reply_to_mentions, twitter_api = twitter_api)
schedule.every(6).hours.do(twitter_jobs.tweet_random_lyrics, twitter_api = twitter_api)
    
def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
