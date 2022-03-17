import numpy as np
import cv2
import threading

#read image
img = cv2.imread('sample.jpg')

threading.Thread

for i, row in enumerate(img):
  for j, pixel in enumerate(img):
    if(i == j or i+j == img.shape[0]):
      img[i][j] = [0,0,0]

cv2.imshow("output", img)
cv2.imwrite("result.jpg", img)