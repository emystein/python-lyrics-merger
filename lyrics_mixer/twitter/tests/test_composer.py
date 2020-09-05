import pytest
from unittest.mock import Mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.twitter.composer import MixLyricsComposer
from lyrics_mixer.song_titles_parser import ParsedArtists
from lyrics_mixer.lyrics_mixer import MixedLyrics
from twitter.tests.model import FakeTweet


def test_compose_reply():
    lyrics_mixer = Mock()

    composer = MixLyricsComposer(lyrics_mixer)

    lyrics_mixer.mix_parsed_song_titles.return_value = 'Blah'

    reply = composer.reply(FakeTweet(1, 'emenendez', 'text'), ParsedArtists(['U2', 'A-ha']))

    assert reply.text == '@emenendez Blah'
