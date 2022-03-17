import numpy as np
import cv2
import random
from threading import Thread

def imgfilter(start, end, rgb):
  for i in range(int(start[0]), int(end[0])):
    for j in range(int(start[1]), int(end[1])):
      r,g,b = img[i,j]
      img[i,j] = [r + rgb[0], g + rgb[1], b + rgb[2]]

#read image
img = cv2.imread('sample.jpg')
img = cv2.resize(img, (500, 400), interpolation = cv2.INTER_AREA)

rows, cols, _ = img.shape
thread_count = 4
threads = []

for i in range(0, thread_count):
  start = [0 + rows / thread_count * i, 0]
  end = [start[0] + rows / thread_count, cols]
  print(start, end)
  rgb = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
  threads.append(Thread(imgfilter(start, end, rgb)))

for thread in threads:
  thread.start()
  

# for i, row in enumerate(img):
#   for j, pixel in enumerate(img):
#     if(i == j or i+j == img.shape[0]):
#       img[i][j] = [0,0,0]

for thread in threads:
  thread.join()

cv2.imshow("output", img)
cv2.imwrite("result.jpg", img)

cv2.waitKey()