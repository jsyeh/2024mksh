# -*- coding: utf-8 -*-
# 我們要在這裡, 把視訊開起來
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    cv2.imshow('opencv08', img)
    # 1000 ms 1秒 
    # 33 ms 對應 1/30 秒(每秒30張)
    if cv2.waitKey(33)==27:
        break # 27對應ESC鍵

cv2.destroyAllWindows()

