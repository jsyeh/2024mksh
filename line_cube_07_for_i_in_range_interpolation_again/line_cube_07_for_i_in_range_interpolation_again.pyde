size(600, 600)
background(255)
for i in range(20, 101, 20):
    line(i, 20, i, 580)
    line(600-i, 20, 600-i, 580)
    line(20, i, 580, i)
    line(20, 600-i, 580, 600-i)
p = []
for i in range(4):
    a = radians(-55+i*90) # 對應的旋轉角度
    p.append(PVector(300+190*cos(a), 300+190*sin(a)))
    ellipse(p[i].x, p[i].y, 10, 10)
for i in range(4):
    line(p[i].x, p[i].y, p[(i+1)%4].x, p[(i+1)%4].y)
for i in range(21):
    p1 = (p[0]*i + p[1]*(20-i))/20 # 照比例內插
    p2 = (p[3]*i + p[2]*(20-i))/20
    line(p1.x, p1.y, p2.x, p2.y)
    p1 = (p[0]*i + p[3]*(20-i))/20 # 照比例內插
    p2 = (p[1]*i + p[2]*(20-i))/20
    line(p1.x, p1.y, p2.x, p2.y)
