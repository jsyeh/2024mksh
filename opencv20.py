# -*- coding: utf-8 -*-
import numpy as np
import cv2

lena = cv2.imread('lena.jpg')
img = lena[:,:]

def myMouse(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        face = lena[y:y+100, x:x+80]
        cv2.imshow('face', face)

cv2.namedWindow('result')
cv2.setMouseCallback('result', myMouse)
while True:
    cv2.imshow('result', img)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
