# -*- coding: utf-8 -*-
import cv2
img = cv2.imread('doll.jpg')
img = cv2.resize(img, (320,240))
cv2.imshow('opencv13', img)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

i = 0
for c1 in [b,g,r]:
    for c2 in [b,g,r]:
        for c3 in [b,g,r]:
            img2 = cv2.merge([c1,c2,c3])
            cv2.imshow('result'+str(i), img2)
            cv2.moveWindow('result'+str(i), (i%5)*200, (i//5)*150 )
            i += 1
            cv2.waitKey(100)
            
cv2.waitKey(0)

for i in range(15):
    cv2.destroyWindow('result'+str(i))

cv2.waitKey(0)

cv2.destroyAllWindows()