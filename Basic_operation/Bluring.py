import cv2
img = cv2.imread("image.png")
imgblur = cv2.blur(img, (5,5), 0)
g_blur=cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow("Image", img)
cv2.imshow("Blur Image", imgblur)
cv2.imshow("Gaussian Blur", g_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


