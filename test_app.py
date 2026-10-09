from app import add, sub, divide
import pytest

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
    
    
def test_divide():
    assert divide(10,2) == 5
    assert divide(12,5) == 2.4
    
# def test_divide_by_zero():
#     with pytest.raises(ValueError):
#         divide(10,0)