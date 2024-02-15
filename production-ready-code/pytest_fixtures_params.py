"""
Learn how to use parameters in fixtures
"""

import pytest


class C:
    def f():
        return 1

    def g():
        return 2


@pytest.fixture(params=(1, 2, 3, 4, 5))
def get_int(request):
    yield request.param
    print("Number was yielded")


def test_get_int(get_int):
    print(f"I get: {get_int}")
