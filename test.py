import pygame

pygame.init()

font = pygame.font.SysFont("Arial", 70)

text = font.render("24", (255, 0, 0), (0, 200, 150))

surface = pygame.display.set_mode((400,300))
 
# Initializing Color
color = (255,0,0)
# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect((20, 20), (100, 100)))
surface.blit(text, (30, 30))

pygame.display.flip()
while True:
    pygame.time.wait(5000)
    break