import pygame
from pygame.draw import *

x = 1700

pygame.init()

BLUE = (175, 238, 238)
GREEN = (60, 179, 113)

FPS = 30
screen = pygame.display.set_mode((1700, 768))
screen.fill(BLUE)

# трава
rect(screen, GREEN, (0, 384, 1700, 384))


        # человек 1
# тело
ellipse(screen, (164, 148, 170), [260, 240, 150, 320], 0)

# руки
line(screen, (0, 0, 0), [378, 270], [490, 420], 1)
line(screen, (0, 0, 0), [292, 270], [188, 420], 1)

# ноги
line(screen, (0, 0, 0), [310, 550], [230, 730], 1)
line(screen, (0, 0, 0), [230, 730], [190, 730], 1)
line(screen, (0, 0, 0), [360, 550], [380, 730], 1)
line(screen, (0, 0, 0), [380, 730], [420, 730], 1)

# голова
circle(screen, (241, 228, 216), (335, 200), 50)



        # человек 2
# тело
polygon(screen, (236, 98, 215), [(680, 240), (580, 560), (780, 560)])

# руки
line(screen, (0, 0, 0), [690, 270], [780, 355], 1)
line(screen, (0, 0, 0), [780, 355], [850, 300], 1)
line(screen, (0, 0, 0), [670, 270], [490, 420], 1)

# ноги
line(screen, (0, 0, 0), [645, 561], [635, 730], 1)
line(screen, (0, 0, 0), [635, 730], [595, 730], 1)
line(screen, (0, 0, 0), [715, 561], [755, 730], 1)
line(screen, (0, 0, 0), [755, 730], [795, 730], 1)

# голова
circle(screen, (241, 228, 216), (680, 200), 50)


        # человек 3
# тело
polygon(screen, (236, 98, 215), [((x-680), 240), ((x-580), 560), ((x-780), 560)])

# руки
line(screen, (0, 0, 0), [(x-690), 270], [(x-780), 355], 1)
line(screen, (0, 0, 0), [(x-780), 355], [(x-850), 300], 1)
line(screen, (0, 0, 0), [(x-670), 270], [(x-490), 420], 1)

# ноги
line(screen, (0, 0, 0), [(x-645), 561], [(x-635), 730], 1)
line(screen, (0, 0, 0), [(x-635), 730], [(x-595), 730], 1)
line(screen, (0, 0, 0), [(x-715), 561], [(x-755), 730], 1)
line(screen, (0, 0, 0), [(x-755), 730], [(x-795), 730], 1)

# голова
circle(screen, (241, 228, 216), ((x-680), 200), 50)


        # человек 4
# тело
ellipse(screen, (164, 148, 170), [(x-260), 240, -150, 320], 0)

# руки
line(screen, (0, 0, 0), [(x-378), 270], [(x-490), 420], 1)
line(screen, (0, 0, 0), [(x-292), 270], [(x-188), 420], 1)

# ноги
line(screen, (0, 0, 0), [(x-310), 550], [(x-230), 730], 1)
line(screen, (0, 0, 0), [(x-230), 730], [(x-190), 730], 1)
line(screen, (0, 0, 0), [(x-360), 550], [(x-380), 730], 1)
line(screen, (0, 0, 0), [(x-380), 730], [(x-420), 730], 1)

# голова
circle(screen, (241, 228, 216), ((x-335), 200), 50)


        # предметы
# мороженное
polygon(screen, (247, 206, 70), [((x-188), 425), ((x-180), 325), ((x-100), 377)])
circle(screen, (234, 51, 36), ((x-153), 325), 25)# красный
circle(screen, (77, 10, 5), ((x-115), 355), 25)# коричневый
circle(screen, (255, 255, 255), ((x-115), 315), 25)# белый


# шарик
line(screen, (0, 0, 0), [188, 420], [142, 150], 1)
polygon(screen, (234, 51, 35), [(142, 150), (152, 65), (72, 95)])
circle(screen, (234, 51, 35), (127, 65), 25)
circle(screen, (234, 51, 35), (91, 80), 25)

# франкенштейн
line(screen, (0, 0, 0), [850, 300], [858.28, 147.5], 1)
polygon(screen, (247, 206, 70), [(858.28, 147.5), (848.25, 22.5), (748.25, 87.5)])
circle(screen, (234, 51, 36), (814.5, 22.5), 31.25)# красный
circle(screen, (77, 10, 5), (767, 60), 31.25)# коричневый
circle(screen, (255, 255, 255), (767, 10), 31.25)# белый


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
