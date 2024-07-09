import pgzrun

HEIGHT = 300
WIDTH = 300

def draw():
    center = 150, 150
    radius = 60
    color = (142, 232, 88)
    screen.draw.circle(center, radius, color)
    
pgzrun.go()