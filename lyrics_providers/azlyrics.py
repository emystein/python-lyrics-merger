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


class ArtistName:
    @staticmethod
    def parse(name):
        if ArtistName.last_name_is_before_first(name):
            return SwappedArtistName(name)
        
        return ArtistName(name)

    @staticmethod
    def last_name_is_before_first(name):
        return ', ' in name

    def __init__(self, name):
        self.name = name


class SwappedArtistName:
    def __init__(self, name):
        self.name = self.swap_first_and_last_names(name)

    def swap_first_and_last_names(self, name):
        return ' '.join(reversed(name.split(', ')))


class Artist:
    @staticmethod
    def named(name):
        return Artist(ArtistName.parse(name).name)

    def __init__(self, name):
        self.name = name

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
        artist = random_artist()
        return artist.random_song_title()


class Song:
    @staticmethod
    def entitled(title):
        return songs.model.Song(title, LazyLoadLyrics(title))


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
