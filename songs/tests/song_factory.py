from songs.model import SongTitle, Song, Lyrics


def stairway_to_heaven_title():
    return SongTitle('Led Zeppelin', 'Stairway to Heaven')


def create_stairway_to_heaven():
    return Song(stairway_to_heaven_title(), Lyrics(read_file('songs/tests/led_zeppelin_-_stairway_to_heaven.txt')))


def born_to_be_wild_title():
    return SongTitle('Steppenwolf', 'Born to be wild')


def create_born_to_be_wild():
    return Song(born_to_be_wild_title(), Lyrics(read_file('songs/tests/steppenwolf_-_born_to_be_wild.txt')))


def read_file(filename):
    file = open(filename, 'r')
    return file.read()
