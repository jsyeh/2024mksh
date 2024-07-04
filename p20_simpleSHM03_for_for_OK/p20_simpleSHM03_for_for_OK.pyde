# p20
def setup():
    size(300,300)
def draw():
    background(255)
    for x in range(0, 300, 20):
        for y in range(0, 300, 20):
            ellipse(x, y, 8, 8)
            r = 4
            a = frameCount*PI/360
            ellipse(x+r*cos(a), y+r*sin(a), 3, 3)
