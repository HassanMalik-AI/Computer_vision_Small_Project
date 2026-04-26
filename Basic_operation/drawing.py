import cv2

img = cv2.imread("image.png")
line=cv2.line(img,(100,200),(200,400),(0,0,255),3)
rectangular=cv2.rectangle(img,(100,200),(200,400),(0,255,0),-1)
#circle=cv2.circle(img,(100,200),(200,400),(255,0,0),3)


cv2.imshow("Image",img)
cv2.imshow("line",line)
cv2.imshow("rectangular",rectangular)
#cv2.imshow("circle",circle)
cv2.waitKey(0)
img.destroyAllWindows()