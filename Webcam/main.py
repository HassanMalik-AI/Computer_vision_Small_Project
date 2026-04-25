import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = video.read()
    
    if not ret:
        print("Failed to grab frame")
        break
    
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(12) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()