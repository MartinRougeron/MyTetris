from shapes import *
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

shapes = [L, T, I, S, SS, O]
shapes_name = ["L", "T", "I", "S", "SS", "O"]
nb_shapes = len(shapes)
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

class Piece(object):
    rows = 5
    columns = 5
    def __init__(self, column, row, shape, name):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.name = name
