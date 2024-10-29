# Here we import a file of opencv im guessing it is a python file
import cv2
import numpy as np


width = 640
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')


while True:
    ignore, frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5)
    print(faces)
    try:
        print(f"faces[0][0] = {faces[0][0]}")
        top_left = (faces[0][0], faces[0][1])
        bottom_right = (faces[0][0] + faces[0][2], faces[0][1] + faces[0][3])  
        color = (0, 0, 255)  # Red color in BGR
        thickness = 2  # Thickness of the square border
        cv2.rectangle(frame, top_left, bottom_right, color, thickness)

    except IndexError:
        print("error")
    # Define the top-left and bottom-right corners of the square
      # x, y coordinates
    # # x, y coordinates

    # # Draw the square (rectangle) on the image
    
    cv2.imshow('Color',frame)
    cv2.moveWindow('Color', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()