import pytest
from unittest.mock import Mock 

@pytest.fixture
def lyrics_library_mock():
	return Mock()

@pytest.fixture
def lyrics_mix_strategy_mock():
	return Mock()
