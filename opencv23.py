# -*- coding: utf-8 -*-
import cv2

cap = cv2.VideoCapture(0)

#lena = cv2.imread('lena.jpg')
#img = lena[:,:]

dollar = cv2.imread('dollar.png')
img2 = dollar[:,:]
cv2.imshow('dollar', img2)

def myMouse(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        face = lena[y:y+100, x:x+80]
        cv2.imshow('face', face)
        img2 = dollar[:,:]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        face = cv2.cvtColor(face, cv2.COLOR_GRAY2BGR)
        img2[100:200, 100:180] = face
        cv2.imshow('dollar', img2)

cv2.namedWindow('result')
cv2.setMouseCallback('result', myMouse)
while True:
    ret, lena = cap.read()
    cv2.imshow('result', lena)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
