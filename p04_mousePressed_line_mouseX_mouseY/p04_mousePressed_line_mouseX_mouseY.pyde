# 存檔 p04_mousePressed_line_mouseX_mouseY
def setup():
    size(500,500)
    background(255,255,232)
def draw():
    if mousePressed:
        line(mouseX, mouseY, pmouseX, pmouseY)
