import numpy
import cv2

img = cv2.imread("test.jpg")
img2 = cv2.imread("test.jpg",0)

cv2.imshow("color",img)
cv2.imshow("gray",img2)
cv2.waitKey(0)
cv2.destroyAllwindows()
