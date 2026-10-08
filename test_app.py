from app import add, sub


# This is unit test
def test_add():
    assert add(2,3) == 5
    assert add(0,1) == 1
    assert add(-1,-1) == -2
    assert add(-2,4) == 2
    assert add(-3,1) == -2
    

def test_sub():
    assert sub(2,4) == -2
    assert sub(9,2) == 7
    assert sub(-1,2) == -3