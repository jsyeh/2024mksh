# 漸近環會出現在圈圈外並開始收縮
t = 100
def myStar(x, y, t):
    cSize = t # dist(mouseX, mouseY, 250, 200)*2
    noFill()
    ellipse(x, y, cSize, cSize)
    fill(193,33,33)
    ellipse(x, y, 40, 40)
x, y = [], []
def setup():
    size(500,400)
    for i in range(30):
        x.append(random(500))
        y.append(random(500))
def draw():
    background(0)
    stroke(92,0,0)
    strokeWeight(6)
    global t
    t -= 2
    if t==0: t = 100
    for i in range(len(x)):
        myStar(x[i], y[i], t)
        
