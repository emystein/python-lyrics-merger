import pytest
from peewee import *
from streams.orm import *


database.create_tables([StreamCursor])


@pytest.fixture(autouse=True)
def with_database_txn():
    with database.atomic() as txn:
        yield
        txn.rollback()


def test_create_stream_cursor():
    cursor = StreamCursor.create(key = 'twitter', position = 1)
    assert StreamCursor.get(StreamCursor.key == 'twitter').position == 1


def test_get_or_create_stream_cursor():
    cursor = StreamCursor.get_or_create(key = 'twitter', position = 1)
    assert StreamCursor.get(StreamCursor.key == 'twitter').position == 1
