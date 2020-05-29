from includes import *
from defines import nb_shapes, Window_height, Window_width
from BuildPieces import FillArray
import sys
import time


pygame.init()

def DrawShape(AllShapes, Choice, BlockSize, Window):
    for i in range(len(AllShapes[Choice].shape)):
        pygame.draw.rect(Window, AllShapes[Choice].color,
    (AllShapes[Choice].position[0] - AllShapes[Choice].shape[i][1] * 50,
    AllShapes[Choice].position[1] - AllShapes[Choice].shape[i][0] * 50,
    BlockSize, BlockSize))

def EventManage():
    for event in pygame.event.get():
        if event.type == QUIT:
        pygame.quit()
        sys.exit(0)

def main():
    BlockSize = 50
    WindowState = 1
    Choice = random.randrange(0, nb_shapes)
    AllShapes = FillArray()
    Window = pygame.display.set_mode((1920, 1080), RESIZABLE)
    Window.fill((0, 0, 0))
    Move = 0
    while WindowState:
        EventManage()
        DrawShape(AllShapes, Choice, BlockSize, Window)
        time.sleep(1/60)
        Move += 1
        if (Move % 45 == 0):
            AllShapes[Choice].position[1] += BlockSize
            Move = 0
        pygame.display.update()
        Window.fill((0, 0, 0))
        print(AllShapes[Choice].position[1])
        continue
    return 0

main()