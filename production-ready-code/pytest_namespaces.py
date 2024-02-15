import pytest


# pytest.arr is None by default as you find in the conftest.py
def test_function_one():
    arr = [1, 2, 3]
    pytest.arr = arr
    assert len(arr) == 3


# now the pytest is populated because the above function was run first
def test_function_two():
    print(pytest.arr)
