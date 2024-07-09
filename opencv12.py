# -*- coding: utf-8 -*-
import cv2
img = cv2.imread('doll.jpg')
cv2.imshow('opencv12', img)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

for c1 in [b,g,r]:
    for c2 in [b,g,r]:
        for c3 in [b,g,r]:
            img2 = cv2.merge([c1,c2,c3])
            cv2.imshow('result', img2)
            cv2.waitKey(1000)
            
cv2.waitKey(0)
cv2.destroyAllWindows()