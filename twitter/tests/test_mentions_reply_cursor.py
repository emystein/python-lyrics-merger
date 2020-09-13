import pytest
from peewee import *
from twitter.persistence import StreamCursor, MentionsReplyCursor


database = SqliteDatabase(':memory:')
database.bind([StreamCursor])
database.create_tables([StreamCursor])


def current_twitter_cursor_position():
    return StreamCursor.get(StreamCursor.key == 'twitter').position


# @pytest.fixture(autouse=True)
# def with_database_txn():
#     with database.atomic() as txn:
#         yield
#         txn.rollback()


def test_get_or_create_mentions_reply_cursor():
    cursor = MentionsReplyCursor()

    assert cursor.position == 1


def test_save_updated_position():
    cursor = MentionsReplyCursor()

    cursor.position = 2

    cursor.save()

    assert current_twitter_cursor_position() == 2


def test_point_to_mention():
    cursor = MentionsReplyCursor()

    cursor.point_to(Mention(id = 2))

    assert current_twitter_cursor_position() == 2


class Mention:
    def __init__(self, id):
        self.id = id
