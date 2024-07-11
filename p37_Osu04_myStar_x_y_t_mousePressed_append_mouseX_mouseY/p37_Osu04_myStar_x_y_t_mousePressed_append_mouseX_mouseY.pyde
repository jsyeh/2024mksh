# 漸近環會出現在圈圈外並開始收縮
def myStar(x, y, t):
    cSize = t # dist(mouseX, mouseY, 250, 200)*2
    noFill()
    ellipse(x, y, cSize, cSize)
    fill(193,33,33)
    ellipse(x, y, 40, 40)
x, y, t = [], [], []
def setup():
    size(500,400)
def draw():
    background(0)
    stroke(92,0,0)
    strokeWeight(6)
    for i in range(len(x)):
        myStar(x[i], y[i], t[i])
        t[i] -= 2
        if t[i]<0: t[i] = 100
def mousePressed():
    x.append(mouseX)
    y.append(mouseY)
    t.append(100)
    
