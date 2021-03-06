import pygame as pg
from pygame.draw import *


pg.init()


s = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

# program


# ФОН
# пляжик
rect(s, (255, 255, 0), (0, 400, 600, 200))

# море
rect(s, (0, 0, 205), (0, 270, 600, 130))

# небо
rect(s, (0, 255, 255), (0, 0, 600, 270))


# ЭЛЕМЕНТЫ
# солнце 
circle(s, (255, 215, 0), (510, 70), 50)

# облако
circle(s, (255, 255, 255), (110, 40), 20)
circle(s, (0, 0, 0), (110, 40), 20, 1)
circle(s, (255, 255, 255), (130, 40), 20)
circle(s, (0, 0, 0), (130, 40), 20, 1)
circle(s, (255, 255, 255), (150, 40), 20)
circle(s, (0, 0, 0), (150, 40), 20, 1)
circle(s, (255, 255, 255), (90, 60), 20)
circle(s, (0, 0, 0), (90, 60), 20, 1)
circle(s, (255, 255, 255), (110, 60), 20)
circle(s, (0, 0, 0), (110, 60), 20, 1)
circle(s, (255, 255, 255), (130, 60), 20)
circle(s, (0, 0, 0), (130, 60), 20, 1)
circle(s, (255, 255, 255), (155, 60), 20)
circle(s, (0, 0, 0), (155, 60), 20, 1)
circle(s, (255, 255, 255), (175, 60), 20)
circle(s, (0, 0, 0), (175, 60), 20, 1)

# зонтик
rect(s, (210, 105, 30), (100, 350, 10, 150))
rect(s, (255,180,180), (100, 350, 10, 40))
polygon(s,(255,180,180),[(100, 280),(100, 280),(150, 400),(80, 400)])
polygon(s,(0, 0, 0),[(100, 280),(100, 280),(150, 400),(80, 400)], 1)


# лодка
rect(s, (139, 69, 19), (300, 300, 180, 50))
rect(s, (0, 0, 0), (300, 300, 180, 50), 1)
polygon(s, (139, 69, 19), [(480, 300), (480, 300), (550, 300), (480, 350)])
polygon(s, (0, 0, 0), [(480, 300), (480, 300), (550, 300), (480, 350)], 1)
rect(s, (0, 0, 0), (400, 200, 10, 100))
polygon(s, (0, 0, 0), [(480, 300), (480, 300), (550, 300), (480, 350)], 1)
polygon(s, (210, 180, 140), [(400, 200), (400, 200), (350, 290), (400, 290)])
circle(s, (255, 255, 255), (500, 315), 10)
circle(s, (0, 0, 0), (500, 315), 10, 2)



pg.display.update()
finished = False 


while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True