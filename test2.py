import cv2

# Replace with the actual URL displayed in DroidCam Client software on your PC
cap = cv2.VideoCapture("http://192.168.243.109:4747/video")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is captured successfully
    if not ret:
        print("Error: Unable to capture frame from DroidCam.")
        break

    # Display the frame (you can replace this with your processing logic)
    cv2.imshow("DroidCam Video", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()