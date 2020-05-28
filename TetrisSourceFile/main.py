from includes import *
from defines import nb_shapes
from BuildPieces import FillArray


pygame.init()

def main():
    window_state = 1
    choice = random.randrange(0, nb_shapes)
    AllShapes = FillArray()
    window = pygame.display.set_mode((640,480), RESIZABLE)
    while window_state:
        for event in pygame.event.get():
            if event.type == QUIT:
                window_state = 0
        continue
    return 0

main()