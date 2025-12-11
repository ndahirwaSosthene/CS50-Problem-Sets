from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar2 = Jar(20)
    assert jar2.capacity == 20
    assert jar2.size == 0
    
    with pytest.raises(ValueError):
        jar3 = Jar(-1)
    with pytest.raises(ValueError):
        jar4 = Jar("hello")
    with pytest.raises(ValueError):
        jar4 = Jar(True)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    
    jar2 = Jar(10)
    jar2.deposit(5)
    assert jar2.size == 5

    jar3 = Jar(5)
    with pytest.raises(ValueError):
        jar3.deposit(10)
    with pytest.raises(ValueError):
        jar3.deposit(0)
    with pytest.raises(ValueError):
        jar3.deposit("Hello")
    with pytest.raises(ValueError):
        jar3.deposit(-1)
    with pytest.raises(ValueError):
        jar3.deposit(True)
    with pytest.raises(ValueError):
        jar3.deposit(False)




def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(5)
    assert jar.size == 0
    
    jar2 = Jar(10)
    jar2.deposit(10)
    jar.withdraw(5)
    assert jar2.size == 5

    jar3 = Jar(20)
    jar3.deposit(15)
    with pytest.raises(ValueError):
        jar3.withdraw(17)
    with pytest.raises(ValueError):
        jar3.withdraw(0)
    with pytest.raises(ValueError):
        jar3.withdraw("Hello")
    with pytest.raises(ValueError):
        jar3.withdraw(-1)
    with pytest.raises(ValueError):
        jar3.withdraw(True)
    with pytest.raises(ValueError):
        jar3.withdraw(False)