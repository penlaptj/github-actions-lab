import pytest
from app import add, greet

def test_add():
    assert add(2, 3) == 99
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_greet():
    assert greet("Joseph") == "Hello, Joseph!"
    assert greet("SG") == "Hello, SG!"
