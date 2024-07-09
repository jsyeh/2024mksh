# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('RGB.jpg')
img = cv2.resize(img, (256,256)) # TODO: 要怎麼把 img 調整大小/縮小
cv2.imshow('RGB', img)

for i in range(12):
    img1 = cv2.applyColorMap(img, i)
    cv2.imshow('img'+str(i), img1)

cv2.waitKey(0)

cv2.destroyAllWindows()