"""
Simple example of setup and teardown. See that setup will be executed first, 
then the test, and finally the teardown. 

To display the print statements in test launch: pytest -s pytest_fixture_setup_terdown_simple.py
"""

import pytest


@pytest.fixture
def setup_teardown():
    print("\n setup")
    yield
    print("teardown")


def test_setup_teardown(setup_teardown):
    print("running test")
