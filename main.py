import random
from _init_ import *
import pygame
from function import *

pygame.display.set_caption("2 0 4 8")


rand_pos1 = random.randint(1, 16)
rand_pos2 = random.randint(1, 16)

while rand_pos2 == rand_pos1:
    rand_pos2 = random.randint(1, 16)
x1, y1 = convert(rand_pos1)
x2, y2 = convert(rand_pos2)

mark[x1][y1] = 1
mark[x2][y2] = 1

# fail immediately before debug
# for i in range(4):
#     for j in range(4):
#         mark[i][j] = j + i + 1
#     mark[i][i] = 2

pygame.event.set_allowed(None)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])


screen.blit(BG, (0, 0))
pygame.display.flip()
lose = False
# tempMark = Cloning(mark)
while running:
    min_val = 1
    screen.blit(BG, (0, 0))
    for i in range(4):
        for j in range(4):
            if mark[i][j] != 0:
                screen.blit(value[mark[i][j]], pos[i][j])
                min_val = min(min_val, mark[i][j])
    pygame.display.flip()
    pygame.event.wait()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            keys = event.key
            if keys == pygame.K_ESCAPE or lose:
                running = False
                break
            elif keys == pygame.K_LEFT:
                p_Left()
            elif keys == pygame.K_RIGHT:
                p_Right()
            elif keys == pygame.K_UP:
                p_Up()
            elif keys == pygame.K_DOWN:
                p_Down()
            if countAppear():
                lose = isLose()
            doing = True
            print("tempMark", tempMark)
            print("mark", mark)
            if (compareList(mark, tempMark)):
                print("same")
                doing = False
            else :
                print("Have diff")
                doing = True
            print("doing: ", doing)
            while doing:
                x, y = convert(random.randint(1,16))
                rand_val = random.randint(1, min_val + 1)
                doing = checkRandValue(x, y, mark, rand_val)
                print (x, y)
            tempMark = Cloning(mark)

    if lose:
        print("in lose")
        screen.blit(Notice, (100, 150))
        pygame.display.flip()
        pygame.time.delay(3000)
        pygame.event.clear()
pygame.quit()