import cv2

# Open laptop camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera could not be opened.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    cv2.imshow("VisionMate AI - Camera Test", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
