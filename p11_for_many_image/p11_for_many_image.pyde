# p10_setup_loadImage_draw_image_global
def setup():
    global imgBG, imgKitty
    size(1000,667) # 用你的background.jpg圖的大小
    imgBG = loadImage('background.jpg')
    imgKitty = loadImage('kitty.png') # 找半透明的png圖
def draw():
    global imgBG, imgKitty
    image(imgBG, 0, 0)
    image(imgKitty, mouseX, mouseY, 200,230)
