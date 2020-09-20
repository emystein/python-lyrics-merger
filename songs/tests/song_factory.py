from songs.model import Song, Lyrics


def create_stairway_to_heaven():
    return Song('Led Zeppelin', 'Stairway to Heaven', Lyrics(read_file('songs/tests/led_zeppelin_-_stairway_to_heaven.txt')))


def create_born_to_be_wild():
    return Song('Steppenwolf', 'Born to be wild', Lyrics(read_file('songs/tests/steppenwolf_-_born_to_be_wild.txt')))


def read_file(filename):
    file = open(filename, 'r')
    return file.read()
