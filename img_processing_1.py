# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 00:34:28 2022
@author: FrankNGUEN
@author: HaiDuc
"""
#------------------------------------------------------------------------------
# import thu vien
#------------------------------------------------------------------------------
import cv2
#------------------------------------------------------------------------------
img   = cv2.imread("images/lidar.JPG")
#------------------------------------------------------------------------------
# 1) Edges
#------------------------------------------------------------------------------
gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray  = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
#------------------------------------------------------------------------------
# 2) Color
#------------------------------------------------------------------------------
color = cv2.bilateralFilter(img, 9, 300, 300)
#------------------------------------------------------------------------------
# 3) Cartoon
#------------------------------------------------------------------------------
cartoon = cv2.bitwise_and(color, color, mask=edges)
#------------------------------------------------------------------------------
#show anh
#------------------------------------------------------------------------------
# write results
cv2.imwrite("images_out/Cartoon.png", cartoon)
cv2.imwrite("images_out/Color.png", color)
cv2.imwrite("images_out/Edges.png", edges)
#show
cv2.imshow("LiDAR image", img)
cv2.imshow("Cartoon", cartoon)
cv2.imshow("color", color)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------------------------------------------------------------