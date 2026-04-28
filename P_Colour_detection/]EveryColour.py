import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# HSV color ranges (tuned for basic detection)
color_ranges = {
    "Red":    [([0, 120, 70], [10, 255, 255]), ([170, 120, 70], [180, 255, 255])],
    "Green":  [([36, 100, 100], [86, 255, 255])],
    "Blue":   [([94, 80, 2], [126, 255, 255])],
    "Yellow": [([15, 100, 100], [35, 255, 255])],
    "Orange": [([5, 100, 100], [15, 255, 255])],
    "Purple": [([129, 50, 70], [158, 255, 255])]
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    output = frame.copy()

    for color_name, ranges in color_ranges.items():
        mask_total = None

        for lower, upper in ranges:
            lower = np.array(lower)
            upper = np.array(upper)

            mask = cv2.inRange(hsv, lower, upper)

            if mask_total is None:
                mask_total = mask
            else:
                mask_total = mask_total + mask

        # Noise removal
        kernel = np.ones((5, 5), np.uint8)
        mask_total = cv2.morphologyEx(mask_total, cv2.MORPH_OPEN, kernel)

        # Find contours
        contours, _ = cv2.findContours(mask_total, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area > 800:
                x, y, w, h = cv2.boundingRect(cnt)

                cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(output, color_name, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Color Detection", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()