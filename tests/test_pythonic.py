from pythonic import __version__
from pythonic.pythonic import *


def test_version():
    assert __version__ == '0.1.0'

def test_factors_one():
    actual = factors_one(100)
    expected = [1, 2, 4, 5, 10, 20, 25, 50, 100]
    assert actual == expected

def test_factors_two():
    actual = [1, 2, 4, 5, 10, 20, 25, 50, 100]
    expected = for idx, factor in factors_two(100):
    assert item == actual[idx]
