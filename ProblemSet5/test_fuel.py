from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert(convert("8/10") == 80)
    assert(convert("1/10") == 10)
    assert(convert("45/55") == 81)
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("100/2")
    with pytest.raises(ValueError):
        convert("100.22")

def test_guage():
    assert(gauge(100) == "F")
    assert(gauge(12) == "12%")
    assert(gauge(1) == "E")
    assert(gauge(0) == "E")
    assert(gauge(99) == "F")
    assert(gauge(98) == "98%")
