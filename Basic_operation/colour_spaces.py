import cv2

img = cv2.imread("image.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)
cv2.imshow("Gray Image", imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()