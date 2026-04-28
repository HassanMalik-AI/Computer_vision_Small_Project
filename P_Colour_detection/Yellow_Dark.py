import cv2
import numpy as np
from PIL import Image

from utils import get_limits

yellow = [0, 255, 255]  # BGR

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = video.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(colour=yellow)

    # FIXED ORDER
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Noise removal
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask1=Image.fromarray(mask)
    width , height = mask1.size

    bbox=mask1.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, "Color Detected", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 5)
 

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
