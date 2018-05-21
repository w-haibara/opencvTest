import cv2
import pylab as plt

im = cv2.imread("test.jpg")
hist = cv2.calcHist([im],[0],None,[256],[0,256])
plt.plot(hist)
plt.xlim([0,256])
plt.show()
