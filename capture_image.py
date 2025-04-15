import cv2

# Set the camera index (change if necessary)
camera_index = 1  

# Open the camera
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print(f"Error: Could not open camera at index {camera_index}")
else:
    # Capture a single frame
    ret, frame = cap.read()

    if ret:
        # Save the image as a JPG file
        filename = "captured_image.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
    else:
        print("Error: Could not capture image")

    # Release the camera
    cap.release()

