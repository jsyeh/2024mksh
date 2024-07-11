# 漸近環會出現在圈圈外並開始收縮
t = 200
def setup():
    size(500,400)
def draw():
    background(0)
    stroke(92,0,0)
    strokeWeight(6)
    noFill()
    global t
    cSize = t # dist(mouseX, mouseY, 250, 200)*2
    t -= 5
    if t==0: t = 200
    ellipse(250, 200, cSize, cSize)
    fill(193,33,33)
    ellipse(250, 200, 40, 40)
