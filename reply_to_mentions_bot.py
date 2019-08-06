import tweepy
import logging
from tweeter import create_api
import time

from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient
from lyrics_mixer.artists_parser import ArtistsParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())

TWEET_LENGTH = 210


def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Replying to {tweet.user.name} about '{tweet.text}'")

            mixed_lyrics = get_mixed_lyrics(tweet)[:TWEET_LENGTH]
            reply_tweet = f"@{tweet.user.name} {mixed_lyrics}"

            api.update_status(
                status=reply_tweet,
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id


def get_mixed_lyrics(tweet):
    artists_parser = ArtistsParser()
    parse_result = artists_parser.parse(tweet.text)
    lyrics_mixer = LyricsMixer(
        WikiaLyricsApiClient(), LineInterleaveLyricsMix())
    mixed_lyrics = lyrics_mixer.mix_random_lyrics_by_artists(
        parse_result.artists[0], parse_result.artists[1])
    return str(mixed_lyrics)


def main():
    api = create_api()
    since_id = 1
    while True:
        print(since_id)
        since_id = check_mentions(api, ["mezcla", "mezclá"], since_id)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
