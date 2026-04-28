import cv2

# Start webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale (intensity-based)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thermal-like colormap
    thermal = cv2.applyColorMap(gray, cv2.COLORMAP_INFERNO)
    # Try others: COLORMAP_JET, COLORMAP_PLASMA, COLORMAP_TURBO

    # Show output
    cv2.imshow("Fake Thermal Camera", thermal)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()