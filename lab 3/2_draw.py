import pygame
from pygame.draw import *

pygame.init()

BLUE = (175, 238, 238)
GREEN = (60, 179, 113)

FPS = 30
screen = pygame.display.set_mode((1032, 768))
screen.fill(BLUE)

#трава
rect(screen, GREEN, (0, 384, 1032, 384))


        #человек слева
#тело
ellipse(screen, (164, 148, 170), [260, 240, 150, 320], 0)

#руки
line(screen, (0, 0, 0), [378, 270], [490, 420], 1)
line(screen, (0, 0, 0), [292, 270], [188, 420], 1)

#ноги
line(screen, (0, 0, 0), [310, 550], [230, 730], 1)
line(screen, (0, 0, 0), [230, 730], [190, 730], 1)
line(screen, (0, 0, 0), [360, 550], [380, 730], 1)
line(screen, (0, 0, 0), [380, 730], [420, 730], 1)

#голова
circle(screen, (241, 228, 216), (335, 200), 50)

#мороженное
polygon(screen, (247, 206, 70), [(188, 425), (180, 325), (100, 377)])
circle(screen, (234, 51, 36), (153, 325), 25)#красный
circle(screen, (255, 255, 255), (115, 315), 25)#белый
circle(screen, (77, 10, 5), (115, 355), 25)#коричневый


        #человек справа
#тело
polygon(screen, (236, 98, 215), [(680, 240), (580, 560), (780, 560)])

#руки
line(screen, (0, 0, 0), [690, 270], [780, 355], 1)
line(screen, (0, 0, 0), [780, 355], [850, 300], 1)
line(screen, (0, 0, 0), [670, 270], [490, 420], 1)

#ноги
line(screen, (0, 0, 0), [645, 561], [635, 730], 1)
line(screen, (0, 0, 0), [635, 730], [595, 730], 1)
line(screen, (0, 0, 0), [715, 561], [755, 730], 1)
line(screen, (0, 0, 0), [755, 730], [795, 730], 1)


#голова
circle(screen, (241, 228, 216), (680, 200), 50)

#шарик
line(screen, (0, 0, 0), [845, 330], [890, 150], 1)
polygon(screen, (234, 51, 35), [(890, 150), (880, 65), (960, 95)])
circle(screen, (234, 51, 35), (905, 65), 25)
circle(screen, (234, 51, 35), (941, 80), 25)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
