smooth(8)
size(700,700)
background(255)
strokeWeight(1.5)
for i in range(20, 100, 20):
    line(i, 20, i, 680)
    line(20, i, 680, i)
    line(700-i, 20, 700-i, 680)
    line(20, 700-i, 680, 700-i)
p = []
for i in range(4):
    a = radians(-55+i*90)
    p.append(PVector(350+250*cos(a), 350+250*sin(a)))
p.append(PVector(600,100)) # p[4] near p[0]
p.append(PVector(600,600)) # p[5] near p[1]
p.append(PVector(100,600)) # p[6] near p[2]
p.append(PVector(100,100)) # p[7] near p[3]
diff = [PVector(80,0), PVector(0,80), PVector(-80,0), PVector(0,-80)]
for i in range(20):
    p1 = (p[0]*(19-i) + p[1]*i)/19
    p2 = (p[3]*(19-i) + p[2]*i)/19
    line(p1.x, p1.y, p2.x, p2.y)
    p1 = (p[0]*(19-i) + p[3]*i)/19
    p2 = (p[1]*(19-i) + p[2]*i)/19
    line(p1.x, p1.y, p2.x, p2.y)
    for k in range(4):
        p1 = (p[0+k]*(19-i) + p[(1+k)%4]*i)/19
        p2 = (p[4+k]*(19-i) + p[4+(1+k)%4]*i)/19
        line(p1.x, p1.y, p2.x, p2.y)
        p1 = (p[4+k]*(19-i) + p[4+(1+k)%4]*i)/19
        p2 = p1 + diff[k]
        line(p1.x, p1.y, p2.x, p2.y)
for i in range(6):
    for k in range(4):
        p1 = (p[0+k]*(5-i) + p[4+k]*i)/5
        p2 = (p[(1+k)%4]*(5-i) + p[4+(1+k)%4]*i)/5
        line(p1.x, p1.y, p2.x, p2.y)
