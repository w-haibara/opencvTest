import numpy
import cv2

img = cv2.imread("test.jpg",0)
cv2.imwrite("test.jpg",img)
