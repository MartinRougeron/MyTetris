from shapes import *
# GLOBALS VARS
Window_width = 1920
Window_height = 1080

shapes = [L, T, I, S, SS, O]
shapes_name = ["L", "T", "I", "S", "SS", "O"]
nb_shapes = len(shapes)
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
class Piece(object):
    rows = 5
    columns = 5
    def __init__(self, column, row, shape, name, position):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.name = name
        self.position = []
        self.position = position
