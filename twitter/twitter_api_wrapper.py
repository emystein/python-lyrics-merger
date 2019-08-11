import twitter

class TwitterApiWrapper(object):
	def __init__(self, twitter_api):
		self.twitter_api = twitter_api
	
	def mentions_timeline(self):
		return self.twitter_api.mentions_timeline

	def update_status(self, tweet):
		self.twitter_api.update_status(tweet[:twitter.MAX_TWEET_LENGTH])

	def reply_tweet_with(self, tweet, reply_text):
	    self.twitter_api.update_status(status = reply_text[:twitter.MAX_TWEET_LENGTH], in_reply_to_status_id = tweet.id)
	