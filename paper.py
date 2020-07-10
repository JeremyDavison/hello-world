import pygame
pygame.init()
surf = pygame.display.set_mode((400, 400))
c = pygame.Color(0,0,200)
surf.fill((255,255,255))
y = 60
for n in range (0, 27):
    for x in range (0, 400):
        surf.set_at ((x, y),c)
    y = y + 20
c = (200, 0, 0)
for y in range(0, 400):
    surf.set_at ((25, y), c)
pygame.display.update()
input()
