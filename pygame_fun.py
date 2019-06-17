import pygame as pg
pg.init()

gameDisplay = pg.display.set_mode((800, 600))
pg.display.set_caption('A bit Racey')
clock = pg.time.Clock()

x = 50
y = 50
width = 40
height = 60
vel = 5

crashed = False

while not crashed:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True

        print(event)

    pg.draw.rect(gameDisplay, (255, 0, 0), (x, y, width, height))

    pg.display.update()

    clock.tick(60)

