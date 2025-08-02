import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0
    # Test case-insensitivity
    assert value("Hello, World") == 0
    # Test with leading/trailing whitespace
    assert value("  hello  ") == 0


def test_value_h():
    assert value("hi") == 20
    assert value("howdy") == 20
    # Test case-insensitivity and whitespace
    assert value("  How's it going? ") == 20


def test_value_other():
    assert value("good morning") == 100
    assert value("what's up?") == 100
    # Test case-insensitivity
    assert value("BONJOUR") == 100
