import cv2

imp = cv2.imread("image.png")

dis = cv2.resize(imp,dsize=(200,200))
cv2.imshow("original",imp)
cv2.imshow("resized",dis)
cv2.waitKey(0)
cv2.destroyAllWindows()


