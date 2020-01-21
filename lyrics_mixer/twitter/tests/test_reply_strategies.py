import pytest
from unittest.mock import Mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.twitter.reply_strategies import MixLyricsReplyStrategy
from lyrics_mixer.mixed_lyrics import MixedLyrics


class User:
    def __init__(self, name):
        self.name = name


class Tweet:
    def __init__(self, username, text):
        self.user = User(username)
        self.text = text


def test_reply(song1, song2):
    lyrics_mixer = Mock()
    mix_command = Mock()

    reply_strategy = MixLyricsReplyStrategy(lyrics_mixer)

    tweet = Tweet('emenendez', 'text')

    mix_command.mix.return_value = MixedLyrics(song1, song2, [], [])

    reply_strategy.write_reply(tweet, mix_command)


def test_exception_on_mix():
    lyrics_mixer = Mock()
    mix_command = Mock()

    reply_strategy = MixLyricsReplyStrategy(lyrics_mixer)

    mix_command.mix.side_effect = RuntimeError('Error mixing songs')

    with pytest.raises(Exception):
        reply_strategy.write_reply("some tweet", mix_command)
