# -*- coding: utf-8 -*-
import cv2
img = cv2.imread('lena.jpg')
cv2.imshow('opencv14', img)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img2)

print( len(img2), len(img2[0]) )

img3 = img2[50:142, : ]
cv2.imshow('img3', img3)

cv2.waitKey(0)

#cv2.destroyWindow('opencv14')
#cv2.destroyWindow('gray')
cv2.destroyAllWindows()