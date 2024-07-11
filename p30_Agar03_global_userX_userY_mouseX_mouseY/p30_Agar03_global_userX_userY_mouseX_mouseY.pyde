def setup():
    size(400,400)
userX, userY = 200.0, 200.0 # 小數點,才精確
def draw():
    global userX, userY
    background(230,235,238)
    stroke(205,216,221)
    for x in range(0,400,50):
        line(x, 0, x, 400)
    for y in range(0,400,50):
        line(0, y, 400, y)
    fill(255,167,7)
    ellipse(userX, userY, 100, 100)
    fill(0, 207,255)
    ellipse(100,100, 60, 60)
    userX = (mouseX+userX*19)/20
    userY = (mouseY+userY*19)/20
