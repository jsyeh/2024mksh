# p19_simpleSHM02_cos_sin_center_radius
def setup():
    size(300,300)
def draw():
    background(255)
    noFill()
    ellipse(150, 150, 200, 200)
    fill(0)
    a = frameCount*PI/360
    ellipse( 150+100*cos(a), 150+100*sin(a), 8, 8)
