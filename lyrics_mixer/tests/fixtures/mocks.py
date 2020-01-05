import pytest
from unittest.mock import Mock 

@pytest.fixture
def lyrics_library_mock():
	return Mock()
