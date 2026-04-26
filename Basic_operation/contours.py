import cv2
import numpy as np

img = cv2.imread("image.png")
img1=cv2.threshold(img,12,25,cv2.THRESH_BINARY_INV)
cv2.imshow('images',img)
cv2.imshow('image1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()