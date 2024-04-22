import pytest


@pytest.mark.parametrize("first_name", "second name", [(1, 2), (2, 3)])
def test_example(first_name, second_name):
    assert first_name + second_name
