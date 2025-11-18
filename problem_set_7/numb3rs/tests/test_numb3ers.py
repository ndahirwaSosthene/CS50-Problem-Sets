from numb3ers import validate

def test_valid_validate():
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.127.0.1") == True

def test_invalid_validate():
    assert validate("260.260.260.260") == False
    assert validate("-1.-1.-1.-1") == False
    assert validate("cat") == False
    assert validate("1234") == False
    assert validate("001.01.0.1") == False
    assert validate("001") == False
