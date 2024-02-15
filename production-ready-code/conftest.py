import pytest


def arr_plugin():
    return None


def pytest_configure():
    pytest.df = arr_plugin()
