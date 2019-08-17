import twitter
import tweepy


class TwitterApiWrapper(object):
    def __init__(self, twitter_api):
        self.twitter_api = twitter_api

    def mentions_since(self, since_id):
        tweets = tweepy.Cursor(self.twitter_api.mentions_timeline, since_id).items()
        mentions = filter(self.is_not_reply, tweets)
        return map(lambda mention: TweetWrapper(self, mention), mentions)

    def is_not_reply(self, tweet):
    	return tweet.in_reply_to_status_id is None

    def update_status(self, tweet):
        self.twitter_api.update_status(tweet[:twitter.MAX_TWEET_LENGTH])

    def reply_tweet_with(self, tweet, reply_text):
        self.twitter_api.update_status(status=reply_text[:twitter.MAX_TWEET_LENGTH], in_reply_to_status_id=tweet.id)


class TweetWrapper(object):
    def __init__(self, twitter_api_wrapper, tweet):
        self.twitter_api_wrapper = twitter_api_wrapper
        self.tweet = tweet
        self.id = tweet.id
        self.user = tweet.user
        self.text = tweet.text

    def reply_using_strategy(self, reply_strategy):
        reply_text = reply_strategy.get_reply_for(self)
        self.reply_with(reply_text)

    def reply_with(self, reply_text):
        self.twitter_api_wrapper.reply_tweet_with(self.tweet, reply_text)