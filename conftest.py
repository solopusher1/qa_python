from main import BooksCollector

import pytest

@pytest.fixture
def collector():
    return BooksCollector()
