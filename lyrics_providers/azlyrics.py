from azapi import AZlyrics
import azlyrics.azlyrics
from functools import cached_property
import json
import random
import songs.model


class Artist:
    @staticmethod
    def random():
        artists_names = json.loads(
            azlyrics.azlyrics.artists(Artist.random_initial()))
        artist_name = random.choice(artists_names)
        return Artist.named(artist_name)

    @staticmethod
    def random_initial():
        return random.choice('abcdefghijklmnopqrstuvwxyz#')

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
        self.cached_all_songs = None

    def all_songs(self):
        if self.cached_all_songs is None:
            api = AZlyrics()
            api.artist = self.name
            all_songs = api.getSongs()

            self.cached_all_songs = [
                Song.entitled(songs.model.SongTitle(self.name, song)) for song in all_songs.keys()
            ]

        return self.cached_all_songs

    def random_song(self):
        return songs.model.Song.random_from(self.all_songs())


class SongTitle:
    @staticmethod
    def random():
        return Artist.random().random_song().title


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
