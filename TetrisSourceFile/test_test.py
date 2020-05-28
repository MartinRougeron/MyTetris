from BuildPieces import FillShape, SameSize

L = [
[0, 0, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 1, 1, 0, 0],
[0, 0, 0, 0, 0],
]
T = [
[0, 0, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
]
I = [
[0, 0, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
]
S = [
[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
]
SS = [
[0, 0, 0, 0, 0],
[0, 1, 1, 0, 0],
[0, 0, 1, 1, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
]
O = [
[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 0, 1, 1, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
]
FalseArray =[
[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 0, 1, 1, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0],
]
FalseArray1 =[
[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 0, 1, 1, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
]
def test_shape_L():
    assert FillShape(0).shape == L
def test_shape_T():
    assert FillShape(1).shape == T
def test_shape_I():
    assert FillShape(2).shape == I
def test_shape_S():
    assert FillShape(3).shape == S
def test_shape_SS():
    assert FillShape(4).shape == SS
def test_shape_O():
    assert FillShape(5).shape == O
def test_not_same_size():
    assert SameSize(FalseArray) == 0
def test_not_same_size1():
    assert SameSize(FalseArray1) == 0
def test_same_size():
    assert SameSize(L) == 1