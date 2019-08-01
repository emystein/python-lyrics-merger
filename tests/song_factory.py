from app.song import Song


def create_song1():
	return Song('Led Zeppelin', 'Stairway to Heaven', read_file('tests/led_zeppelin_-_stairway_to_heaven.txt'))


def create_song2():
	return Song('Steppenwolf', 'Born to be wild', read_file('tests/steppenwolf_-_born_to_be_wild.txt'))


def read_file(filename):
	file = open(filename, 'r')
	return file.read()