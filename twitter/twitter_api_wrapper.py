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
        mentions = filter(self.is_not_reply, tweets)
        wrapped_mentions = list(map(lambda mention: self.wrap_mention(mention), mentions))
        return wrapped_mentions

    def wrap_mention(self, mention):
        return MentionWrapper(self, mention)

    def is_not_reply(self, tweet):
    	return tweet.in_reply_to_status_id is None

    def update_status(self, tweet):
        self.twitter_api.update_status(tweet[:twitter.MAX_TWEET_LENGTH])

    def reply_tweet_with(self, tweet, reply_text):
        self.twitter_api.update_status(status=reply_text[:twitter.MAX_TWEET_LENGTH], in_reply_to_status_id=tweet.id)

    def reply_to_mentions(self, mentions, reply_strategy):
        new_since_id = 1
        for tweet in mentions:
            reply = reply_strategy.get_reply_for(tweet)
            self.twitter_api.reply_tweet_with(tweet, reply)
            new_since_id = tweet.id
        return new_since_id


class MentionWrapper(object):
    def __init__(self, twitter_api, tweet):
        self.twitter_api = twitter_api
        self.tweet = tweet

    def reply_with(self, reply_strategy):
        reply = reply_strategy.get_reply_for(self.tweet)
        self.twitter_api.reply_tweet_with(self.tweet, reply)
        return self.tweet.id
