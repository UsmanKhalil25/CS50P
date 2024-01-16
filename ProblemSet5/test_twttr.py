from twttr import shorten

def test_shorten():
    assert(shorten("twitter") == "twttr")
    assert(shorten("Usman") == "smn")
    assert(shorten("Vega") == "Vg")
