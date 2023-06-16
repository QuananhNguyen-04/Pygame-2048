
import pygame

pygame.init()

BG_WIDTH = 629
BG_HEIGHT = 629
NUM_SIZE = BG_WIDTH * 8 / 37
BARRIER = BG_WIDTH / 37

# ICON = pygame.image.load('') chưa có file thì sẽ gặp lỗi
myFont = pygame.font.SysFont("timesnewroman", 100)
Notice = myFont.render("YOU LOSE", False, (0, 0, 0), (255, 0, 0))
# rect = pygame.
BG = pygame.image.load("./pic/BG.png") 
BG = pygame.transform.scale(BG, (BG_WIDTH, BG_HEIGHT))
n2 = pygame.image.load("./pic/n2.png")
n2 = pygame.transform.scale(n2, (NUM_SIZE, NUM_SIZE))
n4 = pygame.image.load("./pic/n4.png")
n4 = pygame.transform.scale(n4, (NUM_SIZE, NUM_SIZE))
n8 = pygame.image.load("./pic/n8.png")
n8 = pygame.transform.scale(n8, (NUM_SIZE, NUM_SIZE))
n16 = pygame.image.load("./pic/n16.png")
n16 = pygame.transform.scale(n16, (NUM_SIZE, NUM_SIZE))
n32 = pygame.image.load("./pic/n32.png")
n32 = pygame.transform.scale(n32, (NUM_SIZE, NUM_SIZE))
n64 = pygame.image.load("./pic/n64.png")
n64 = pygame.transform.scale(n64, (NUM_SIZE, NUM_SIZE))
clock = pygame.time.Clock()

screen = pygame.display.set_mode((BG_WIDTH, BG_HEIGHT))

value = [0, n2, n4, n8, n16, n32, n64]

POS1 = (BARRIER                     , BARRIER)
POS2 = (BARRIER * 2 + NUM_SIZE      , BARRIER)
POS3 = (BARRIER * 3 + NUM_SIZE * 2  , BARRIER)
POS4 = (BARRIER * 4 + NUM_SIZE * 3  , BARRIER)
POS5 = (BARRIER                     , BARRIER * 2 + NUM_SIZE)
POS6 = (BARRIER * 2 + NUM_SIZE      , BARRIER * 2 + NUM_SIZE)
POS7 = (BARRIER * 3 + NUM_SIZE * 2  , BARRIER * 2 + NUM_SIZE)
POS8 = (BARRIER * 4 + NUM_SIZE * 3  , BARRIER * 2 + NUM_SIZE)
POS9 = (BARRIER                     , BARRIER * 3 + NUM_SIZE * 2)
POS10 = (BARRIER * 2 + NUM_SIZE     , BARRIER * 3 + NUM_SIZE * 2)
POS11 = (BARRIER * 3 + NUM_SIZE * 2 , BARRIER * 3 + NUM_SIZE * 2)
POS12 = (BARRIER * 4 + NUM_SIZE * 3 , BARRIER * 3 + NUM_SIZE * 2)
POS13 = (BARRIER                    , BARRIER * 4 + NUM_SIZE * 3)
POS14 = (BARRIER * 2 + NUM_SIZE     , BARRIER * 4 + NUM_SIZE * 3)
POS15 = (BARRIER * 3 + NUM_SIZE * 2 , BARRIER * 4 + NUM_SIZE * 3)
POS16 = (BARRIER * 4 + NUM_SIZE * 3 , BARRIER * 4 + NUM_SIZE * 3)
pos=[[POS1, POS2, POS3, POS4],[POS5, POS6, POS7, POS8],[POS9, POS10, POS11, POS12],[POS13, POS14, POS15, POS16]]

running = True