import pytest
from peewee import *
from lyrics_mixer.orm import *


database.create_tables([StreamCursor])

@pytest.fixture(autouse=True)
def with_database_txn():
    with database.atomic() as txn:
        yield
        txn.rollback()


def test_cursor_model():
    cursor = StreamCursor.create(key = 'tweeter', position = 1)
    cursor.save()

    assert StreamCursor.select().count() == 1
    retrieved_cursor = StreamCursor.get(StreamCursor.key == 'tweeter')
    assert retrieved_cursor.position == 1
