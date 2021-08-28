from azapi import AZlyrics
import azlyrics.azlyrics
from functools import cached_property, cache
import json
import logging
import random
import songs.model

logger = logging.getLogger()


def random_artist():
    artist_names = artist_names_with_initial(random_artist_initial())
    artist_name = random.choice(artist_names)
    return Artist.named(artist_name)


def random_artist_initial():
    return random.choice('abcdefghijklmnopqrstuvwxyz#')


def artist_names_with_initial(initial):
    return json.loads(azlyrics.azlyrics.artists(initial))


class AZLyricsLibrary:
    """Bridge to external lyrics provider, like AZLyrics"""

    def get_lyrics(self, song_title):
        logger.info(f'Retrieving lyrics of: {song_title}')
        return Song.entitled(song_title)

    def get_random_lyrics(self):
        return self.get_lyrics(SongTitle.random())

    def get_random_lyrics_by_artist(self, artist_name):
        return Artist.named(artist_name).random_song()

    def pick_using(self, lyrics_pickers):
        return lyrics_pickers.pick_from(self)


class ArtistNameParser:
    def parse(self, name):
        if self.last_name_is_before_first(name):
            return SwappedArtistName(name)
        else:
            return ArtistName(name)

    def last_name_is_before_first(self, name):
        return ', ' in name


class ArtistName:
    def __init__(self, name):
        self.name = name

    def normalized(self):
        return self.name


class SwappedArtistName:
    def __init__(self, name):
        self.name = name

    def normalized(self):
        return self.swap_first_and_last_names(self.name)

    def swap_first_and_last_names(self, name):
        return ' '.join(reversed(name.split(', ')))


class Artist:
    @staticmethod
    def named(potential_name):
        artist_name = ArtistNameParser().parse(potential_name)
        return Artist(artist_name)

    def __init__(self, artist_name):
        self.name = artist_name.normalized()

    @cache
    def all_songs(self):
        return [self.song_named(song) for song in self.all_songs_from_api()]

    def all_songs_from_api(self):
        api = AZlyrics()
        artist_code = ArtistCodeDictionary().translate(self.name)
        api.artist = artist_code
        return api.getSongs().keys()

    def song_named(self, song):
        return Song.entitled(songs.model.SongTitle(self.name, song))

    def random_song(self):
        return songs.model.Song.random_from(self.all_songs())

    def random_song_title(self):
        return self.random_song().title


class ArtistCodeDictionary:
    def __init__(self):
        self.codes_by_names = {
            'U2': 'u2band'
        }

    def translate(self, name):
        return self.codes_by_names.get(name, name)


class SongTitle:
    @staticmethod
    def random():
        return random_artist().random_song_title()


class Song:
    @staticmethod
    def entitled(song_title):
        return songs.model.Song(song_title, Lyrics(song_title))


class Lyrics(songs.model.Lyrics):
    def __init__(self, title):
        self.title = title

    @property
    def paragraphs(self):
        return songs.model.Paragraphs(self.text)

    @property
    def lines(self):
        return self.paragraphs.lines

    @cached_property
    def text(self):
        api = AZlyrics()
        api.artist = self.title.artist
        api.title = self.title.title
        api.getLyrics()
        return api.lyrics
