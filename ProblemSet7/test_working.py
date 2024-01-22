from working import convert
from working import convert_util


def test_convert_util():
    assert(convert_util("12",":00","AM") == "00:00")
    assert(convert_util("12",":23","AM") == "00:23")
    assert(convert_util("12",":00","PM") == "12:00")
    assert(convert_util("1",":56","AM") == "01:56")
    assert(convert_util("1",":46","PM") == "13:46")


def test_convert():
    assert(convert("9:00 AM to 5:00 PM") == "09:00 to 17:00")
    assert(convert("9 AM to 5 PM") == "09:00 to 17:00")

