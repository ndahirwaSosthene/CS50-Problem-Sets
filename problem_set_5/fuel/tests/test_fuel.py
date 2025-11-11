from fuel import convert, gauge
import pytest


def test_convert_calid():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0
    assert convert("1/4") == 33
    assert convert("2/4") == 67
    

def test_convert_invalid_format():  
    with pytest.raises(ValueError):
        convert("three/four")

def test_convert_zero_division():
    with pytest.raises(ValueError):
        convert("1.5/2")

    with pytest.raises(ValueError):
        convert("1/2/3")

    with pytest.raises(ValueError):
        convert("1")

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/4")

    with pytest.raises(ValueError):
        convert("1/-4")

    with pytest.raises(ValueError):
        convert("-1/-4")

def test_convert_x_greater_than_y():  
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert_zero_division():
    with pytest.raises(ValueError):
        convert("10/1")


def test_gauge_percentage():
    assert gauge(2) == "2%"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"

def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"