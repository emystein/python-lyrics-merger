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
    parsed_song_titles = Mock()
    mix_command = Mock()

    reply_strategy = MixLyricsReplyStrategy(lyrics_mixer)

    tweet = Tweet('emenendez', 'text')

    parsed_song_titles.mix_command.return_value = mix_command

    expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])

    mix_command.mix.return_value = expected_mixed_lyrics 

    result = reply_strategy.write_reply(tweet, parsed_song_titles)

    assert result == f"@{tweet.user.name} {expected_mixed_lyrics}"


def test_exception_on_mix():
    lyrics_mixer = Mock()
    parsed_song_titles = Mock()
    mix_command = Mock()

    reply_strategy = MixLyricsReplyStrategy(lyrics_mixer)

    parsed_song_titles.mix_command.return_value = mix_command

    mix_command.mix.side_effect = RuntimeError('Error mixing songs')

    with pytest.raises(Exception):
        reply_strategy.write_reply("some tweet", parsed_song_titles)
