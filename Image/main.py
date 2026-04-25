import cv2
images=cv2.imread("Image\image.jpg")

print(images.shape)
print(cv2.imwrite("image.jpg",images))
cv2.imshow("Image",images)
cv2.waitKey(0)
cv2.destroyAllWindows()

