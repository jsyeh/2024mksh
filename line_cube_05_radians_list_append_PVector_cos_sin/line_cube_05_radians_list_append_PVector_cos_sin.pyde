size(600, 600)
background(255)
for i in range(20, 101, 20):
    line(i, 20, i, 580)
    line(600-i, 20, 600-i, 580)
    line(20, i, 580, i)
    line(20, 600-i, 580, 600-i)
ellipse(300, 300, 380, 380)
ellipse(300, 300, 10, 10)
p = []
for i in range(4):
    a = radians(-55+i*90) # 對應的旋轉角度
    p.append(PVector(300+190*cos(a), 300+190*sin(a)))
    ellipse(p[i].x, p[i].y, 10, 10)
