# p13_for_list_append
def setup():
    global imgBG, imgKitty
    size(1000,667) # 用你的background.jpg圖的大小
    imgBG = loadImage('background.jpg')
    imgKitty = loadImage('kitty.png') # 找半透明的png圖
def draw():
    global imgBG, imgKitty
    image(imgBG, 0, 0)
    for i in range(len(x)):
        image(imgKitty, x[i], y[i], 200, 230)
    image(imgKitty, mouseX, mouseY, 200,230)
x = [] # x = [0]*10
y = [] # y = [0]*10
#N = 0
def mousePressed():
    x.append(mouseX) #global N
    y.append(mouseY) #x[N], y[N] = mouseX, mouseY
    #N += 1
