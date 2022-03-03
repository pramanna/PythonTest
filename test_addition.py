from pickle import ADDITEMS
from addtion import add


def test_add():
    import addtion
    assert addtion.add(1,1) == 2
    assert addtion.add(-1,-1) == -2

def test_sub():
    import addtion
    assert addtion.sub(2,1) == 1
    assert addtion.sub(1, 1) == 0

