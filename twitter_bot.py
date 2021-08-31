import logging
import schedule
import sys
import time
from lyrics_providers.azlyrics import AZLyricsLibrary
from lyrics_mixer.lyrics_mixer import LyricsMixer
from lyrics_mixer.lyrics_mix_strategies import LineInterleaveLyricsMix
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser
import twitter_bot.jobs
from twitter_bot.persistence import MentionsReplyCursor
from twitter_bot.twitter import TwitterApi, MentionHistory, Composer

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
schedule_logger = logging.getLogger('schedule')
schedule_logger.setLevel(level=logging.WARNING)

logging.info('Starting up')

twitter_bot.persistence.connect_to_database()

# advance reply cursor to a mention already replied
reply_cursor = MentionsReplyCursor()
if reply_cursor.position < 1363510795649318917:
    reply_cursor.position = 1363510795649318917
    reply_cursor.save()

twitter_api = TwitterApi(twitter_bot.twitter.create_tweepy_api())

tweet_parser = SongTitlesParser(SongTitlesSplitter())

lyrics_mixer = LyricsMixer(
    AZLyricsLibrary(), LineInterleaveLyricsMix())

composer=Composer(twitter_api, tweet_parser, lyrics_mixer)

schedule.every().minute.do(twitter_bot.jobs.reply_to_mentions,
                           mention_history=MentionHistory(twitter_api, reply_cursor),
                           composer=composer)

schedule.every(4).hours.do(twitter_bot.jobs.tweet_random_lyrics,
                           twitter_api=twitter_api,
                           lyrics_mixer=lyrics_mixer,
                           composer=composer).run()


def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
