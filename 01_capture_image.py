import cv2
import os

# create a directory to store the captured images
if not os.path.exists('captured_images'):
    os.makedirs('captured_images')

# initialize the camera
cap = cv2.VideoCapture(2)

# check if camera was opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# loop through frames to capture multiple images
for i in range(120):
    # read the frame from the camera
    ret, frame = cap.read()

    # if frame is read correctly, save the image
    if ret == True:
        filename = f'captured_images/image_{i}.jpg'
        cv2.imwrite(filename, frame)
        print(f"Image {i} captured")

# release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
