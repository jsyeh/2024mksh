size(600, 600)
background(255)
for i in range(20, 101, 20):
    line(i, 20, i, 580)
    line(600-i, 20, 600-i, 580)
    line(20, i, 580, i)
    line(20, 600-i, 580, 600-i)

ellipse(300, 300, 380, 380)
ellipse(300, 300, 10, 10)
