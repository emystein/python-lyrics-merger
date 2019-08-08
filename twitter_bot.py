import logging
import schedule
import time
from tweeter import create_api
from reply_to_mentions_bot import MixLyricsReplyStrategy, check_mentions
from lyrics_mixer.orm import StreamCursor

from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix
from wikia.lyrics_api_client import WikiaLyricsApiClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

api = create_api()

reply_strategy = MixLyricsReplyStrategy()


def reply_to_mentions():
    logger.info("Replying to mentions")
    cursor, created = StreamCursor.get_or_create(key='tweeter')
    cursor.position = check_mentions(api, cursor.position, reply_strategy)
    cursor.save()


MAX_TWEET_LENGTH = 280


def tweet_random_lyrics():
    print("About to mix lyrics")
    lyrics_mixer = LyricsMixer(WikiaLyricsApiClient(), LineInterleaveLyricsMix())
    mixed_lyrics = lyrics_mixer.mix_two_random_lyrics()
    tweet = str(mixed_lyrics)[:MAX_TWEET_LENGTH]
    api.update_status(tweet)


schedule.every(2).to(8).hours.do(tweet_random_lyrics)
# schedule.every().minute.do(reply_to_mentions)


def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
