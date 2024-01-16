from bank import value

def test_value():
    assert(value("Hello, How are you?") == 0)
    assert(value("Hi, How are you?") == 20)
    assert(value("What is happening?") == 100)
    assert(value("What are you doing?") == 100) 
