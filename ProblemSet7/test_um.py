from um import count


def test_count():
    assert(count("um") == 1)
    assert(count("") == 0)
    assert(count("world um world") == 1)
    assert(count("world um um um world") == 3)
    assert(count("um umum um") == 2)
    assert(count("yummy") == 0)
    assert(count("umum umum ummmmm um") == 1)
    assert(count("um?") == 1)
    assert(count("Um, thanks for the album.") == 1)
    assert(count("Um, thanks, um...") == 2)
    