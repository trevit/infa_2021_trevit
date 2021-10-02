import pygame
from pygame.draw import *

pygame.init()

WHITE = (255, 255, 255)

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(WHITE)

circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (0, 0, 0), (200, 200), 150, 2)

circle(screen, (255, 0, 0), (130, 150), 30)
circle(screen, (0, 0, 0), (130, 150), 10)
circle(screen, (0, 0, 0), (130, 150), 30, 2)

circle(screen, (255, 0, 0), (270, 150), 20)
circle(screen, (0, 0, 0), (270, 150), 10)
circle(screen, (0, 0, 0), (270, 150), 20, 2)

polygon(screen, (0, 0, 0), [(50, 70), (175, 150), (180, 140), (55, 60)])
polygon(screen, (0, 0, 0), [(350, 100), (225, 150), (220, 140), (345, 90)])

rect(screen, (0, 0, 0), (100, 250, 200, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
