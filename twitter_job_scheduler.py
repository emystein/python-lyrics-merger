import schedule
import time
import twitter
import twitter_reply_with_lyrics
import twitter_random_lyrics    

twitter_api = twitter.create_api()
    
schedule.every().minute.do(twitter_reply_with_lyrics.reply_to_mentions, twitter_api = twitter_api)
schedule.every(6).hours.do(twitter_random_lyrics.tweet_random_lyrics, twitter_api = twitter_api)
    
def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
