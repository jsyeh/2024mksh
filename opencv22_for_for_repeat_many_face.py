# -*- coding: utf-8 -*-
import numpy as np
import cv2

lena = cv2.imread('lena.jpg')
img = lena[:,:]
result = np.zeros((1000, 800, 3), np.uint8)
cv2.imshow('result2', result)
def myMouse(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        face = lena[y:y+100, x:x+80]
        cv2.imshow('face', face)
        #img2 = dollar[:,:]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        face = cv2.cvtColor(face, cv2.COLOR_GRAY2BGR)
        for i in range(10):
            for j in range(10):
                result[i*100:i*100+100, j*80:j*80+80] = face
        cv2.imshow('result2', result)

cv2.namedWindow('result')
cv2.setMouseCallback('result', myMouse)
while True:
    cv2.imshow('result', img)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
