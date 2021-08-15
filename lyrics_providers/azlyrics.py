from azapi import AZlyrics
import azlyrics.azlyrics
from functools import cached_property, cache
import json
import random
import songs.model


class Artist:
    @staticmethod
    def random():
        random_initial = random.choice('abcdefghijklmnopqrstuvwxyz#')
        artists_names = json.loads(azlyrics.azlyrics.artists(random_initial))
        artist_name = random.choice(artists_names)
        return Artist.named(artist_name)

    @staticmethod
    def named(name):
        if ', ' in name:
            name = Artist.swap_first_and_last_name(name)

        return Artist(name)

    @staticmethod
    def swap_first_and_last_name(name):
        return ' '.join(reversed(name.split(', ')))

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
        artist = Artist.random()
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
