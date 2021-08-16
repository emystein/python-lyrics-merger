from azapi import AZlyrics
import azlyrics.azlyrics
from functools import cached_property, cache
import json
import random
import songs.model


def random_artist():
    artist_names = artist_names_with_initial(random_artist_initial())
    artist_name = random.choice(artist_names)
    return Artist.named(artist_name)


def random_artist_initial():
    return random.choice('abcdefghijklmnopqrstuvwxyz#')


def artist_names_with_initial(initial):
    return json.loads(azlyrics.azlyrics.artists(initial))


class ArtistNameParser:
    def parse(self, name):
        if self.last_name_is_before_first(name):
            return SwappedArtistName(name)
        
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
        api = AZlyrics()
        api.artist = self.name
        all_songs = api.getSongs()

        return [Song.entitled(songs.model.SongTitle(self.name, song)) for song in all_songs.keys()]

    def random_song(self):
        return songs.model.Song.random_from(self.all_songs())

    def random_song_title(self):
        return self.random_song().title


class SongTitle:
    @staticmethod
    def random():
        return random_artist().random_song_title()


class Song:
    @staticmethod
    def entitled(song_title):
        return songs.model.Song(song_title, LazyLoadLyrics(song_title))


class LazyLoadLyrics(songs.model.Lyrics):
    def __init__(self, title):
        self.title = title

    @cached_property
    def text(self):
        api = AZlyrics()
        api.artist = self.title.artist
        api.title = self.title.title
        api.getLyrics()
        return api.lyrics
