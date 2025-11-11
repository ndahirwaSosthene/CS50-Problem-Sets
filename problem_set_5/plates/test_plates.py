from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True

def test_invalid_leading_zero():
    assert is_valid("CS05") == False

def test_invalid_characters():
    assert is_valid("PI3.14") == False

def test_invalid_length():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_numbers_at_end():
    assert is_valid("CS50P") == False