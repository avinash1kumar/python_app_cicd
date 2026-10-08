from app import add


# This is unit test
def test_add():
    assert add(2,3) == 5
    assert add(0,1) == 1
    assert add(-1,-1) == -2
    assert add(-2,4) == 2
    assert add(-3,1) == -2