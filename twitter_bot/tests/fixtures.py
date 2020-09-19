import pytest
from unittest.mock import Mock

@pytest.fixture
def tweet():
    tweet = Mock()
    tweet.text = '@lyricsmixer mix Led Zeppelin and Steppenwolf'
    return tweet