"""
Understand setup teardown with pytest fixture. Lets create a temporary directory
in test phase, and delete as soon as test is concluded
"""

import tempfile
import pytest


class C:
    def f():
        return 1

    def g():
        return 2


@pytest.fixture
def temporary_dir():
    with tempfile.TemporaryDirectory() as tempdir:
        yield tempdir
        print(
            "now we can delete the new directoy. No need because it a tempdir in this case"
        )


@pytest.fixture
def c_instance():
    return C()


def test_temporary_dir(temporary_dir):
    print(temporary_dir)
