from numb3rs import validate

def test_validate():
    assert(validate("1.2.3.4") == True)
    assert(validate("255.255.255.255") == True)
    assert(validate("0.0.0.0") == True)
    assert(validate("0,0,0,0") == False)
    assert(validate("256.255.255.255") == False)
    assert(validate("dog") == False)
    assert(validate("Random text,,.=") == False)
    assert(validate("     1.2.34.44") == True)
    assert(validate("     1.2.34.44         ") == True)


    
