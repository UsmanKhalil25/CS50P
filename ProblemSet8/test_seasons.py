import pytest
from seasons import get_minutes


def test_get_minutes():
    assert(get_minutes("2003-07-21") == "ten million, seven hundred eighty-seven thousand forty")
    assert(get_minutes("2010-09-21") == "seven million, fifteen thousand, six hundred eighty")
    assert(get_minutes("2000-01-01") == "twelve million, six hundred fifty-four thousand, seven hundred twenty")

def test_get_minutes_error():
    with pytest.raises(SystemExit):
        get_minutes("1-jan-2045")
        get_minutes("cat")
        get_minutes("january 23 2405")
