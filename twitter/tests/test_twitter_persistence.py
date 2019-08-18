import pytest
from peewee import *
from streams.persistence import *
from twitter.persistence import MentionsReplyCursor


database.create_tables([StreamCursor])


@pytest.fixture(autouse=True)
def with_database_txn():
    with database.atomic() as txn:
        yield
        txn.rollback()


def test_get_or_create_mentions_reply_cursor():
    cursor = MentionsReplyCursor()
    assert StreamCursor.get(StreamCursor.key == 'twitter').position == 1
    assert cursor.position == 1


def test_update_position():
    cursor = MentionsReplyCursor()
    assert cursor.position == 1

    cursor.position = 2

    assert cursor.position == 2


def test_save_updated_position():
    cursor = MentionsReplyCursor()

    cursor.position = 2

    cursor.save()
    assert StreamCursor.get(StreamCursor.key == 'twitter').position == 2


def test_point_to_mention():
    cursor = MentionsReplyCursor()
    mention = FakeMention(id = 2)

    cursor.point_to(mention)

    assert StreamCursor.get(StreamCursor.key == 'twitter').position == 2


class FakeMention(object):
    def __init__(self, id):
        self.id = id
