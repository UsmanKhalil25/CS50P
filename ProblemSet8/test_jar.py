import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert(jar.capacity == 12)


def test_str():
    jar = Jar()
    jar.deposit(10)
    assert(str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪")


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert(jar.size == 5)
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert(jar.size == 3)
    with pytest.raises(ValueError):
        jar.withdraw(10)