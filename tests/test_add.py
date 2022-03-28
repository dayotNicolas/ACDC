import pytest

from projet_ACDC.add_function import add

@pytest.mark.skip()
def test_add():
    assert add(3, 5) == 8
