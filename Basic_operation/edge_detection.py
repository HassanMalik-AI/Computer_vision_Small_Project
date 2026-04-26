import cv2
import numpy as np

img = cv2.imread("image.png")
edge_detection = cv2.Canny(img,200,100)

kernel = np.ones((5,5), np.uint8)
dilote = cv2.dilate(edge_detection, kernel, iterations=1)
erode = cv2.erode(edge_detection, kernel, iterations=1)

cv2.imshow('image', img)
cv2.imshow('edge', edge_detection)
cv2.imshow('dilate', dilote)
cv2.imshow('erode', erode)
cv2.waitKey(0)
cv2.destroyAllWindows()