#import cv2
#
#def list_available_cameras(max_cameras=10):
#    available_cameras = []
#    for index in range(max_cameras):
#        cap = cv2.VideoCapture(index)
#        if cap.isOpened():
#            available_cameras.append(index)
#            cap.release()
#    return available_cameras
#
#cameras = list_available_cameras()
#print("Available camera indices:", cameras)
import cv2

# Try different indices if 0 doesn't work (e.g., /dev/video1 -> index 1)
camera_index = 1  
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print(f"Failed to open camera at index {camera_index}")
else:
    print(f"Camera {camera_index} opened successfully!")

# Release the camera
cap.release()

