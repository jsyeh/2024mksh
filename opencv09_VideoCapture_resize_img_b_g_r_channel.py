# -*- coding: utf-8 -*-
import cv2
cap = cv2.VideoCapture(0)

while True: # 一直執行
    ret, img = cap.read()
    img = cv2.resize(img, (320,240))
    b = img[:,:,0]
    g = img[:,:,1]
    r = img[:,:,2]
    cv2.imshow('img', img)
    cv2.imshow('b', b)
    cv2.imshow('g', g)
    cv2.imshow('r', r)
    
    if cv2.waitKey(33)==27:
        break
    
cv2.destroyAllWindows()
    
