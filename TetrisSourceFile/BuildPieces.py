from defines import Piece, shapes_name, shapes, nb_shapes

def FillShape(position):
    return Piece(5, 5, shapes[position], shapes_name[position])

def SameSize(Array):
    row = len(Array)
    for i in range(0, row - 1):
        if (len(Array[i]) != len(Array[i + 1])):
            return 0
    return 1

def TransfromToVector(Array):
    row = len(Array)
    if (SameSize(Array) == 0):
        return 0
    columns = len(Array[0])
    NewArray = []
    for y in range(row):
        for x in range(columns):
            if (Array[y][x] != 0):
                NewArray.append([x - 2, y - 2])
    return NewArray

def FillArray():
    AllShapes = []
    for i in range(nb_shapes):
        AllShapes.append(FillShape(i))
    for i in range(nb_shapes):
        AllShapes[i].shape = TransfromToVector(AllShapes[i].shape)
    return AllShapes