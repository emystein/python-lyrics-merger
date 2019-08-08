import pytest
from peewee import *
from lyrics_mixer.orm import *


database.create_tables([StreamCursor])

@pytest.fixture(autouse=True)
def with_database_txn():
    with database.atomic() as txn:
        yield
        txn.rollback()


def test_stream_cursor_orm():
    cursor = StreamCursor.create(key = 'tweeter', position = 1)
    assert StreamCursor.get(StreamCursor.key == 'tweeter').position == 1
