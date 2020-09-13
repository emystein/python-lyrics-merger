from azapi import AZlyrics
import azlyrics.azlyrics
import json
import logging
import random
import songs.model


logger = logging.getLogger()


class Artist:
    @staticmethod
    def random():
        artist_initial = Artist.random_initial()
        artists_names = json.loads(azlyrics.azlyrics.artists(artist_initial))
        artist_name = random.choice(artists_names)

        logger.info(f'Random Artist name: {artist_name}')

        return Artist.named(artist_name)

    @staticmethod
    def random_initial():
        return random.choice('abcdefghijklmnopqrstuvwxyz#')

    @staticmethod
    def named(name):
        if ', ' in name:
            last_name_first_name_swapped = ' '.join(reversed(name.split(', ')))
            return Artist(last_name_first_name_swapped)
        else:
            return Artist(name)

    def __init__(self, name):
        logger.info(f'Artist named: {name}')

        self.name = name

    def all_songs(self):
        logger.info(f'Retrieving all songs by: {self.name}')

        api = AZlyrics()
        api.artist = self.name
        all_songs = api.getSongs()

        logger.info(f'Retrieved {len(all_songs)} songs')

        return [songs.model.Song(self.name, songs.model.SongTitle(self.name, song), LazyLoadLyrics(self.name, song)) for song in all_songs.keys()]

    def random_song(self):
        return songs.model.Song.random_from(self.all_songs())


class SongTitle:
    @staticmethod
    def random():
        return Artist.random().random_song().title


class Song:
    @staticmethod
    def entitled(title):
        print(f'Retrieving song: {title.artist} - {title.title}')
        logger.info(f'Retrieving song: {str(title)}')

        api = AZlyrics()
        api.artist = title.artist
        api.title = title.title
        api.getLyrics()

        return songs.model.Song(title.artist, title, songs.model.Lyrics(api.lyrics))


class LazyLoadLyrics(songs.model.Lyrics):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.loaded_text = None
    
    @property
    def text(self):
        if self.loaded_text is None:
            api = AZlyrics()
            api.artist = self.artist
            api.title = self.title
            api.getLyrics()
            self.loaded_text = api.lyrics
        
        return self.loaded_text

        