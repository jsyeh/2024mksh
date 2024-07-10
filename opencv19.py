# -*- coding: utf-8 -*-
import numpy as np # 數值的資料結構
import cv2

img = np.zeros( (512,512,3), np.uint8 )
cv2.namedWindow('opencv19')
cv2.imshow('opencv19', img)

def draw_circle(e, x, y, f, p):
    global mouseX, mouseY # 要給外面的座標
    if e == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 10, (255,0,0), -1)
        print('double click')

cv2.setMouseCallback('opencv19', draw_circle)
while True: # while迴圈一直做
    cv2.imshow('opencv19', img)
    if cv2.waitKey(33)==27: # 按ESC鍵離開
        break

# cv2.waitKey(0)
cv2.destroyAllWindows()


