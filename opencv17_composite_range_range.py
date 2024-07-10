# -*- coding: utf-8 -*-
import cv2

lena = cv2.imread('lena.jpg')
cv2.imshow('opencv17', lena)

dollar = cv2.imread('dollar.png')
cv2.imshow('result', dollar)

face = lena[50:150, 50:150]
cv2.imshow('face', face)

dollar[100:200, 100:200] = face
cv2.imshow('result', dollar)


cv2.waitKey(0)
cv2.destroyAllWindows()
