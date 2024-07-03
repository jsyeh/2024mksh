# p12_for_many_image_list_def_mousePressed
def setup():
    global imgBG, imgKitty
    size(1000,667) # 用你的background.jpg圖的大小
    imgBG = loadImage('background.jpg')
    imgKitty = loadImage('kitty.png') # 找半透明的png圖
def draw():
    global imgBG, imgKitty
    image(imgBG, 0, 0)
    for i in range(10):
        image(imgKitty, x[i], y[i], 200, 230)
    image(imgKitty, mouseX, mouseY, 200,230)
x = [0]*10
y = [0]*10
N = 0
def mousePressed():
    global N
    x[N], y[N] = mouseX, mouseY
    N += 1
