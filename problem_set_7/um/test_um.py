import pytest

from um import count

def test_valid_count():
    assert count("um") == 1
    assert count("album") == 0
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2