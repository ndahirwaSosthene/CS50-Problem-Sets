from bank import value

def main():
    test_value()

def test_value():
    assert("hello") == "$0"
    assert("hi") == "$20"
    assert("geez") == "$100"
    assert(",") == "$100"
    assert(1) == "$100" 