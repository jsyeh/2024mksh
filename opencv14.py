# -*- coding: utf-8 -*-
import cv2
img = cv2.imread('lena.jpg')
cv2.imshow('opencv14', img)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img2)

cv2.waitKey(0)

cv2.destroyWindow('opencv14')