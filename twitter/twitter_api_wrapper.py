import logging
import twitter
import tweepy


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class TwitterApiWrapper(object):
    def __init__(self, twitter_api):
        self.twitter_api = twitter_api

    def mentions_since(self, since_id):
        tweets = tweepy.Cursor(self.twitter_api.mentions_timeline, since_id=since_id).items()
        return filter(self.is_not_reply, tweets)

    def is_not_reply(self, tweet):
    	return tweet.in_reply_to_status_id is None

    def update_status(self, tweet):
        self.twitter_api.update_status(tweet[:twitter.MAX_TWEET_LENGTH])

    def reply_tweet_with(self, tweet, reply_text):
        self.twitter_api.update_status(status=reply_text[:twitter.MAX_TWEET_LENGTH], in_reply_to_status_id=tweet.id)

	def reply_to_mentions_since(self, since_id, reply_strategy):
		logger.info(f"Checking mentions since: {since_id}")

		new_since_id = since_id
		mentions = self.mentions_since(since_id)
		for tweet in mentions:
			reply_text = reply_strategy.get_reply_for(tweet)
			twitter_api.reply_tweet_with(tweet, reply_text)
			new_since_id = tweet.id
		return new_since_id
