from plates import is_valid

def test_is_valid():
    assert(is_valid("CS50") == True)
    assert(is_valid("CS05") == False)
    assert(is_valid("2334") == False)
    assert(is_valid("GOODBYE") == False)
    assert(is_valid("AA99A") == False)
    assert(is_valid("AA999") == True)
    