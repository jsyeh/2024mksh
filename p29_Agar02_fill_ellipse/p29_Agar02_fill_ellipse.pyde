def setup():
    size(400,400)
def draw():
    background(230,235,238)
    stroke(205,216,221)
    for x in range(0,400,50):
        line(x, 0, x, 400)
    for y in range(0,400,50):
        line(0, y, 400, y)
    fill(255,167,7)
    ellipse(200, 200, 100, 100)
    fill(0, 207,255)
    ellipse(100,100, 60, 60)
