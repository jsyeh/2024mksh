dotX, dotY, dotS = [], [], []
userX, userY, userS = 200.0, 200.0, 30.0 # 小數點,才精確
def setup():
    size(400,400)
    for i in range(50):
        dotX.append(random(400))
        dotY.append(random(400))
        dotS.append(random(3,20))
def draw():
    global userX, userY, userS
    background(230,235,238)
    stroke(205,216,221)
    for x in range(0,400,50):
        line(x, 0, x, 400)
    for y in range(0,400,50):
        line(0, y, 400, y)
    fill(255,167,7)
    ellipse(userX, userY, userS, userS)
    fill(0, 207,255)
    for i in range(len(dotX)):
        ellipse(dotX[i], dotY[i], dotS[i],dotS[i])
        if dist(userX, userY, dotX[i], dotY[i]) < (userS+dotS[i])/2:
            #if dotS[i]!=0: userS += dotS[i]
            if dotS[i]!=0: userS = sqrt(userS*userS + dotS[i]*dotS[i])
            dotS[i] = 0
    userX = (mouseX+userX*19)/20
    userY = (mouseY+userY*19)/20
