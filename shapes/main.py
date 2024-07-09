import pgzrun

from random import randint
WIDTH = 300
HEIGHT = 300

def draw():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    width = 250
    height = (width - 20)
    for i in range(20):
        rect = Rect((0, 0), (width, height))
        rect.center = 150, 150
        screen.draw.rect(rect, (r,g,b))
        width -= 10
        height += 10
pgzrun.go()