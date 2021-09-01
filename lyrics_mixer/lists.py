from itertools import chain


def flatten(list_of_lists):
    return list(chain(*list_of_lists))
